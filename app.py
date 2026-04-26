"""
Flask Backend API
=================
RESTful API for Movie Rating Analysis with MongoDB integration.

Author: Data Science Team
Date: April 2026

Run with: python app.py
"""

from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from data_loader import MongoDBManager
from recommendation_system import CollaborativeFiltering
from utils import DataValidator, DataProcessor

# Initialize Flask app
app = Flask(__name__, template_folder='frontend', static_folder='frontend/static')
CORS(app)

# Global variables
db_manager = None
movies_df = None
ratings_df = None
cf_system = None


# ==================== API Routes ====================

@app.route('/')
def index():
    """Serve main page."""
    return render_template('index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    try:
        stats = db_manager.get_db_stats() if db_manager else None
        return jsonify({
            'status': 'healthy',
            'database': 'connected' if stats else 'disconnected',
            'database_stats': stats
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/stats', methods=['GET'])
def get_statistics():
    """Get overall statistics."""
    try:
        if movies_df is None or ratings_df is None:
            return jsonify({'error': 'Data not loaded'}), 400
        
        stats = {
            'total_movies': len(movies_df),
            'total_ratings': len(ratings_df),
            'total_users': int(ratings_df['userId'].nunique()),
            'average_rating': float(ratings_df['rating'].mean()),
            'min_rating': float(ratings_df['rating'].min()),
            'max_rating': float(ratings_df['rating'].max()),
            'std_rating': float(ratings_df['rating'].std())
        }
        
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movies/top-rated', methods=['GET'])
def get_top_rated_movies():
    """Get top rated movies."""
    try:
        limit = request.args.get('limit', 20, type=int)
        min_ratings = request.args.get('min_ratings', 1, type=int)
        
        if db_manager:
            movies = db_manager.get_top_movies(limit, min_ratings)
            return jsonify({
                'movies': movies,
                'count': len(movies)
            }), 200
        else:
            # Fallback if MongoDB not available
            movie_stats = ratings_df.groupby('movieId').agg({
                'rating': ['mean', 'count', 'sum']
            }).reset_index()
            movie_stats.columns = ['movieId', 'avg_rating', 'rating_count', 'total_ratings']
            movie_stats = movie_stats[movie_stats['rating_count'] >= min_ratings].sort_values('avg_rating', ascending=False).head(limit)
            
            result = movie_stats.merge(movies_df[['movieId', 'title', 'genres']], on='movieId')
            return jsonify({
                'movies': result.to_dict('records'),
                'count': len(result)
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movies/popular', methods=['GET'])
def get_popular_movies():
    """Get most popular movies."""
    try:
        limit = request.args.get('limit', 20, type=int)
        
        if db_manager:
            movies = db_manager.get_popular_movies(limit)
            return jsonify({
                'movies': movies,
                'count': len(movies)
            }), 200
        else:
            movie_stats = ratings_df.groupby('movieId').agg({
                'rating': ['mean', 'count', 'sum']
            }).reset_index()
            movie_stats.columns = ['movieId', 'avg_rating', 'rating_count', 'total_ratings']
            movie_stats = movie_stats.sort_values('rating_count', ascending=False).head(limit)
            
            result = movie_stats.merge(movies_df[['movieId', 'title', 'genres']], on='movieId')
            return jsonify({
                'movies': result.to_dict('records'),
                'count': len(result)
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movies/search', methods=['GET'])
def search_movies():
    """Search movies by title."""
    try:
        query = request.args.get('q', '', type=str).lower()
        limit = request.args.get('limit', 10, type=int)
        
        if not query:
            return jsonify({'error': 'Query parameter required'}), 400
        
        results = movies_df[movies_df['title'].str.lower().str.contains(query, na=False)].head(limit)
        
        # Add rating info
        movie_stats = ratings_df.groupby('movieId').agg({
            'rating': ['mean', 'count']
        }).reset_index()
        movie_stats.columns = ['movieId', 'avg_rating', 'rating_count']
        
        results = results.merge(movie_stats, on='movieId', how='left').fillna(0)
        
        return jsonify({
            'results': results.to_dict('records'),
            'count': len(results)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/genres/stats', methods=['GET'])
def get_genre_statistics():
    """Get genre statistics."""
    try:
        if db_manager:
            genres = db_manager.get_genre_statistics()
            return jsonify({
                'genres': genres,
                'count': len(genres)
            }), 200
        else:
            # Fallback calculation
            genre_stats = []
            for _, row in movies_df.iterrows():
                genres = row['genres'].split('|')
                movie_ratings = ratings_df[ratings_df['movieId'] == row['movieId']]['rating']
                
                for genre in genres:
                    if genre and genre != '(no genres listed)':
                        genre_stats.append({
                            'genre': genre,
                            'avg_rating': float(movie_ratings.mean()) if len(movie_ratings) > 0 else 0,
                            'rating_count': len(movie_ratings)
                        })
            
            # Aggregate by genre
            genre_df = pd.DataFrame(genre_stats)
            if len(genre_df) > 0:
                genre_agg = genre_df.groupby('genre').agg({
                    'avg_rating': 'mean',
                    'rating_count': 'sum'
                }).reset_index().sort_values('avg_rating', ascending=False)
                return jsonify({
                    'genres': genre_agg.to_dict('records'),
                    'count': len(genre_agg)
                }), 200
            else:
                return jsonify({'genres': [], 'count': 0}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ratings/distribution', methods=['GET'])
def get_rating_distribution():
    """Get rating distribution."""
    try:
        bins = [0, 1, 2, 3, 4, 5.1]
        labels = ['0-1', '1-2', '2-3', '3-4', '4-5']
        
        distribution = pd.cut(ratings_df['rating'], bins=bins, labels=labels, right=False)
        counts = distribution.value_counts().sort_index()
        
        result = {
            label: int(count) for label, count in zip(counts.index, counts.values)
        }
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    """Get recommendations for a user."""
    try:
        n_recommendations = request.args.get('limit', 5, type=int)
        method = request.args.get('method', 'user_based', type=str)
        
        if cf_system is None:
            return jsonify({'error': 'Recommendation system not initialized'}), 500
        
        if method == 'user_based':
            recommendations = cf_system.recommend_user_based(user_id, n_recommendations)
        elif method == 'item_based':
            recommendations = cf_system.recommend_item_based(user_id, n_recommendations)
        elif method == 'hybrid':
            rec_summary = cf_system.get_recommendation_summary(user_id, n_recommendations)
            recommendations = rec_summary['hybrid_recommendations']
        else:
            return jsonify({'error': 'Invalid method'}), 400
        
        # Add movie details
        if len(recommendations) > 0:
            recommendations = recommendations.merge(
                movies_df[['movieId', 'title', 'genres']],
                on='movieId',
                how='left'
            )
            return jsonify({
                'user_id': user_id,
                'recommendations': recommendations.to_dict('records'),
                'count': len(recommendations)
            }), 200
        else:
            return jsonify({
                'user_id': user_id,
                'recommendations': [],
                'count': 0
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    """Get detailed information about a movie."""
    try:
        movie = movies_df[movies_df['movieId'] == movie_id]
        
        if len(movie) == 0:
            return jsonify({'error': 'Movie not found'}), 404
        
        movie_info = movie.iloc[0].to_dict()
        
        # Add rating stats
        movie_ratings = ratings_df[ratings_df['movieId'] == movie_id]['rating']
        movie_info['avg_rating'] = float(movie_ratings.mean()) if len(movie_ratings) > 0 else 0
        movie_info['rating_count'] = len(movie_ratings)
        movie_info['total_ratings'] = float(movie_ratings.sum())
        
        # Add similar movies if available
        if cf_system:
            similar = cf_system.find_similar_movies(movie_id, 5)
            if len(similar) > 0:
                similar_with_details = similar.merge(
                    movies_df[['movieId', 'title', 'genres']],
                    left_on='similar_movieId',
                    right_on='movieId'
                )
                movie_info['similar_movies'] = similar_with_details.to_dict('records')
        
        return jsonify(movie_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/user/<int:user_id>/ratings', methods=['GET'])
def get_user_ratings(user_id):
    """Get all ratings for a specific user."""
    try:
        user_ratings = ratings_df[ratings_df['userId'] == user_id]
        
        if len(user_ratings) == 0:
            return jsonify({'error': 'User not found'}), 404
        
        # Add movie details
        user_ratings_with_movies = user_ratings.merge(
            movies_df[['movieId', 'title', 'genres']],
            on='movieId'
        )
        
        return jsonify({
            'user_id': user_id,
            'ratings': user_ratings_with_movies.to_dict('records'),
            'count': len(user_ratings_with_movies),
            'average_rating': float(user_ratings['rating'].mean())
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/data/info', methods=['GET'])
def get_data_info():
    """Get information about loaded data."""
    try:
        return jsonify({
            'data_loaded': movies_df is not None and ratings_df is not None,
            'movies_count': len(movies_df) if movies_df is not None else 0,
            'ratings_count': len(ratings_df) if ratings_df is not None else 0,
            'mongodb_connected': db_manager is not None and db_manager.db is not None
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """Update movie details."""
    try:
        global movies_df, ratings_df
        
        data = request.get_json()
        
        # Validate input
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Check if movie exists
        if movie_id not in movies_df['movieId'].values:
            return jsonify({'error': 'Movie not found'}), 404
        
        # Update the movie in the dataframe
        idx = movies_df[movies_df['movieId'] == movie_id].index
        
        if 'title' in data and data['title']:
            movies_df.at[idx[0], 'title'] = data['title']
        
        if 'genres' in data and data['genres']:
            movies_df.at[idx[0], 'genres'] = data['genres']
        
        if 'description' in data:
            if 'description' not in movies_df.columns:
                movies_df['description'] = ''
            movies_df.at[idx[0], 'description'] = data['description']
        
        # Update rating if provided (update average rating for this movie in ratings)
        if 'rating' in data and data['rating'] is not None:
            # Update the rating average for display purposes
            # Note: This updates an aggregated view, not individual ratings
            if 'avg_rating' not in movies_df.columns:
                movies_df['avg_rating'] = 0.0
            movies_df.at[idx[0], 'avg_rating'] = float(data['rating'])
        
        # Try to update in MongoDB if available
        if db_manager and db_manager.db:
            try:
                db_manager.update_movie(movie_id, data)
            except Exception as e:
                print(f"Warning: Could not update in MongoDB: {e}")
        
        return jsonify({
            'message': 'Movie updated successfully',
            'movieId': movie_id,
            'updated_fields': list(data.keys())
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== Initialization ====================

def load_data():
    """Load data on startup."""
    global db_manager, movies_df, ratings_df, cf_system
    
    print("Loading data...")
    
    try:
        # Try to load from CSV files
        data_dir = 'data'
        movies_path = os.path.join(data_dir, 'movies.csv')
        ratings_path = os.path.join(data_dir, 'ratings.csv')
        
        if os.path.exists(movies_path) and os.path.exists(ratings_path):
            movies_df = pd.read_csv(movies_path)
            ratings_df = pd.read_csv(ratings_path)
            print(f"✓ Loaded data: {len(movies_df)} movies, {len(ratings_df)} ratings")
        else:
            print("⚠️  Data files not found in 'data' directory")
            return False
        
        # Try to connect to MongoDB
        try:
            db_manager = MongoDBManager()
            if db_manager.db:
                db_manager.insert_movies(movies_df)
                db_manager.insert_ratings(ratings_df)
                print("✓ MongoDB data loaded")
        except Exception as e:
            print(f"⚠️  MongoDB not available: {e}")
        
        # Initialize recommendation system
        cf_system = CollaborativeFiltering(ratings_df)
        cf_system.calculate_user_similarity()
        cf_system.calculate_item_similarity()
        print("✓ Recommendation system initialized")
        
        return True
    
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return False


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


# ==================== Main ====================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("MOVIE RATING ANALYSIS - FLASK API")
    print("="*60 + "\n")
    
    # Load data
    if load_data():
        print("\n" + "="*60)
        print("Starting Flask server...")
        print("Open browser at: http://localhost:5000")
        print("="*60 + "\n")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("\n✗ Failed to load data. Please ensure data files exist in 'data/' directory")
        print("Generate sample data by running: python data/sample_data_generator.py")
