"""
Sample Data Generator
=====================
Generate sample MovieLens-like data for testing and demonstration.

Author: Data Science Team
Date: April 2026
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

class SampleDataGenerator:
    """Generate sample movie ratings data for demonstration."""
    
    # Popular movie titles
    MOVIE_TITLES = [
        ("The Shawshank Redemption", "Drama"),
        ("The Godfather", "Crime|Drama"),
        ("The Dark Knight", "Action|Crime|Drama"),
        ("Pulp Fiction", "Crime|Drama"),
        ("Forrest Gump", "Drama|Romance"),
        ("Inception", "Action|Sci-Fi|Thriller"),
        ("The Matrix", "Action|Sci-Fi"),
        ("Interstellar", "Adventure|Drama|Sci-Fi"),
        ("The Avengers", "Action|Adventure|Sci-Fi"),
        ("Avatar", "Action|Adventure|Fantasy|Sci-Fi"),
        ("Titanic", "Drama|Romance"),
        ("Jurassic Park", "Action|Adventure|Sci-Fi"),
        ("The Lion King", "Animation|Adventure|Drama|Family"),
        ("Frozen", "Animation|Adventure|Comedy|Family|Musical"),
        ("Finding Nemo", "Animation|Adventure|Comedy|Family"),
        ("Toy Story", "Animation|Adventure|Comedy|Family"),
        ("The Notebook", "Drama|Romance"),
        ("Gladiator", "Action|Adventure|Drama"),
        ("Braveheart", "Adventure|Drama|History|War"),
        ("The Silence of the Lambs", "Crime|Drama|Thriller"),
        ("Se7en", "Crime|Drama|Mystery|Thriller"),
        ("Saving Private Ryan", "Drama|War"),
        ("Schindler's List", "Biography|Drama|History"),
        ("Casablanca", "Drama|Romance|War"),
        ("Citizen Kane", "Drama|Mystery"),
        ("The Godfather Part II", "Crime|Drama"),
        ("12 Angry Men", "Drama"),
        ("Gone with the Wind", "Drama|History|Romance"),
        ("Vertigo", "Mystery|Romance|Thriller"),
        ("Rear Window", "Mystery|Thriller"),
        ("Psycho", "Horror|Thriller"),
        ("The Exorcist", "Horror"),
        ("The Conjuring", "Horror|Mystery|Thriller"),
        ("A Nightmare on Elm Street", "Horror"),
        ("Halloween", "Horror"),
        ("The Sixth Sense", "Drama|Mystery|Thriller"),
        ("Memento", "Mystery|Thriller"),
        ("The Usual Suspects", "Crime|Drama|Mystery|Thriller"),
        ("Fight Club", "Drama|Thriller"),
        ("American Psycho", "Crime|Drama|Thriller"),
        ("Requiem for a Dream", "Drama"),
        ("Trainspotting", "Crime|Drama"),
        ("Platoon", "Drama|War"),
        ("Full Metal Jacket", "Drama|War"),
        ("Dr. Strangelove", "Comedy|War"),
        ("2001: A Space Odyssey", "Adventure|Sci-Fi"),
        ("A Clockwork Orange", "Crime|Drama|Sci-Fi"),
        ("The Shining", "Horror|Thriller"),
        ("Apocalypse Now", "Drama|War"),
        ("The French Connection", "Crime|Drama|Thriller"),
    ]
    
    @staticmethod
    def generate_movies_data(n_movies=50):
        """
        Generate movies dataset.
        
        Parameters:
        -----------
        n_movies : int
            Number of movies to generate
        
        Returns:
        --------
        pd.DataFrame : Movies dataframe
        """
        selected_movies = np.random.choice(
            len(SampleDataGenerator.MOVIE_TITLES),
            min(n_movies, len(SampleDataGenerator.MOVIE_TITLES)),
            replace=False
        )
        
        movies_data = []
        for idx, movie_idx in enumerate(selected_movies, 1):
            title, genres = SampleDataGenerator.MOVIE_TITLES[movie_idx]
            movies_data.append({
                'movieId': idx,
                'title': title,
                'genres': genres
            })
        
        df = pd.DataFrame(movies_data)
        print(f"✓ Generated {len(df)} movies")
        return df
    
    @staticmethod
    def generate_ratings_data(movies_df, n_users=100, ratings_per_user_range=(10, 40)):
        """
        Generate ratings dataset.
        
        Parameters:
        -----------
        movies_df : pd.DataFrame
            Movies dataframe
        n_users : int
            Number of users to generate
        ratings_per_user_range : tuple
            Range of ratings per user (min, max)
        
        Returns:
        --------
        pd.DataFrame : Ratings dataframe
        """
        ratings_data = []
        
        # Rating distribution (higher ratings more likely)
        rating_values = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
        rating_weights = np.array([0.02, 0.03, 0.05, 0.08, 0.12, 0.15, 0.18, 0.20, 0.12, 0.05])
        
        base_timestamp = int(datetime(2020, 1, 1).timestamp())
        
        for user_id in range(1, n_users + 1):
            # Random number of ratings for this user
            n_ratings = np.random.randint(
                ratings_per_user_range[0],
                ratings_per_user_range[1]
            )
            
            # Random movie selection
            rated_movies = np.random.choice(
                movies_df['movieId'].values,
                min(n_ratings, len(movies_df)),
                replace=False
            )
            
            for movie_id in rated_movies:
                rating = np.random.choice(rating_values, p=rating_weights)
                timestamp = base_timestamp + np.random.randint(0, 365*24*3600)
                
                ratings_data.append({
                    'userId': user_id,
                    'movieId': int(movie_id),
                    'rating': float(rating),
                    'timestamp': timestamp
                })
        
        df = pd.DataFrame(ratings_data)
        print(f"✓ Generated {len(df)} ratings from {n_users} users")
        return df
    
    @staticmethod
    def generate_and_save(output_dir='data', n_movies=50, n_users=100):
        """
        Generate and save both datasets.
        
        Parameters:
        -----------
        output_dir : str
            Output directory
        n_movies : int
            Number of movies
        n_users : int
            Number of users
        """
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate movies
        movies_df = SampleDataGenerator.generate_movies_data(n_movies)
        movies_path = os.path.join(output_dir, 'movies.csv')
        movies_df.to_csv(movies_path, index=False)
        print(f"✓ Saved movies to: {movies_path}")
        
        # Generate ratings
        ratings_df = SampleDataGenerator.generate_ratings_data(movies_df, n_users)
        ratings_path = os.path.join(output_dir, 'ratings.csv')
        ratings_df.to_csv(ratings_path, index=False)
        print(f"✓ Saved ratings to: {ratings_path}")
        
        return movies_df, ratings_df


if __name__ == "__main__":
    # Generate sample data
    print("Generating sample MovieLens-like data...")
    SampleDataGenerator.generate_and_save(
        output_dir='data',
        n_movies=50,
        n_users=150
    )
    print("\n✓ Sample data generation complete!")
