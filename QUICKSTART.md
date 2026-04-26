# 🚀 Quick Start Guide - Movie Rating Analysis

## Prerequisites
- Python 3.8 or higher
- MongoDB (optional, for database integration)
- Git (optional)

---

## Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate Sample Data (if needed)
```bash
python data/sample_data_generator.py
```
This creates sample `movies.csv` and `ratings.csv` files in the `data/` folder.

### Step 3: Start MongoDB (Optional)
```bash
# Windows
mongod

# Linux/Mac
mongod --config /usr/local/etc/mongod.conf
```

---

## Running the Project

### Option A: Jupyter Notebook (Recommended for Learning)
```bash
jupyter notebook notebook/movie_analysis.ipynb
```
This runs the complete analysis with all visualizations and insights.

### Option B: Flask Web Application
```bash
python app.py
```
Then open your browser and navigate to:
```
http://localhost:5000
```

### Option C: Command Line (Python Scripts)
```bash
# Generate data
python data/sample_data_generator.py

# Run analysis modules individually
python -c "from src.data_loader import *; print('Modules loaded successfully')"
```

---

## Project Structure

```
MovieRatingAnalysis/
│
├── 📁 data/
│   ├── movies.csv                 # Movie data (auto-generated)
│   ├── ratings.csv                # Ratings data (auto-generated)
│   └── sample_data_generator.py   # Data generation script
│
├── 📁 notebook/
│   └── movie_analysis.ipynb       # Main Jupyter Notebook (⭐ START HERE)
│
├── 📁 src/
│   ├── __init__.py
│   ├── data_loader.py             # MongoDB integration
│   ├── recommendation_system.py    # Recommendation algorithms
│   └── utils.py                   # Utility functions
│
├── 📁 frontend/
│   ├── index.html                 # Web interface
│   └── static/                    # Static assets
│
├── 📁 output/
│   └── (Generated visualizations)
│
├── app.py                         # Flask backend API
├── requirements.txt               # Python dependencies
├── README.md                      # Full documentation
└── QUICKSTART.md                  # This file
```

---

## Usage Examples

### Example 1: View Top-Rated Movies
```python
import pandas as pd
from src.data_loader import MongoDBManager

# Load data
movies_df = pd.read_csv('data/movies.csv')
ratings_df = pd.read_csv('data/ratings.csv')

# Calculate statistics
movie_stats = ratings_df.groupby('movieId')['rating'].agg(['mean', 'count'])
movie_stats = movie_stats.merge(movies_df, on='movieId')
top_movies = movie_stats.sort_values('mean', ascending=False).head(20)
print(top_movies[['title', 'mean']])
```

### Example 2: Get Movie Recommendations
```python
from src.recommendation_system import CollaborativeFiltering

# Initialize system
cf = CollaborativeFiltering(ratings_df)
cf.calculate_user_similarity()
cf.calculate_item_similarity()

# Get recommendations for user 5
recommendations = cf.recommend_user_based(user_id=5, n_recommendations=10)
print(recommendations)
```

### Example 3: Store Data in MongoDB
```python
from src.data_loader import load_data_to_mongodb

# Load and store data
manager = load_data_to_mongodb(movies_df, ratings_df)

# Query top movies
top_movies = manager.get_top_movies(limit=20)
print(top_movies)

manager.close()
```

---

## Web Interface Features

When running `python app.py`, you can access:

1. **Overview Dashboard** - Dataset statistics and rating distribution
2. **Top Rated** - Highest-rated movies
3. **Most Popular** - Most-watched movies
4. **Genres** - Genre analysis and trends
5. **Search** - Search movies by title
6. **Recommendations** - Get personalized recommendations by user ID

---

## API Endpoints (Flask)

### Statistics
```
GET /api/stats
GET /api/data/info
```

### Movies
```
GET /api/movies/top-rated?limit=20&min_ratings=5
GET /api/movies/popular?limit=20
GET /api/movies/search?q=Inception&limit=10
GET /api/movie/<movie_id>
```

### Genres
```
GET /api/genres/stats
```

### Ratings
```
GET /api/ratings/distribution
GET /api/user/<user_id>/ratings
```

### Recommendations
```
GET /api/recommendations/<user_id>?method=user_based&limit=5
GET /api/recommendations/<user_id>?method=item_based&limit=5
GET /api/recommendations/<user_id>?method=hybrid&limit=5
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "MongoDB connection failed"
**Solution:**
MongoDB is optional. The project works without it. Make sure MongoDB service is running if you want to use it.

### Issue: "Port 5000 already in use"
**Solution:**
```python
# In app.py, change the port:
app.run(port=5001)  # Use a different port
```

### Issue: "FileNotFoundError: data/movies.csv"
**Solution:**
```bash
python data/sample_data_generator.py
```

---

## Performance Tips

1. **Reduce dataset size** for faster processing:
   ```python
   movies_df = movies_df.head(1000)
   ratings_df = ratings_df.head(50000)
   ```

2. **Use MongoDB indexing** for faster queries

3. **Cache recommendations** to avoid recalculation

4. **Use vectorized operations** with NumPy and Pandas

---

## Next Steps

1. ✅ Run the Jupyter Notebook for complete analysis
2. ✅ Explore the web interface with Flask
3. ✅ Modify data or parameters
4. ✅ Add more features (see Future Scope in README.md)
5. ✅ Deploy to production (cloud platforms)

---

## Learning Resources

- 📖 [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- 📖 [Collaborative Filtering Guide](https://en.wikipedia.org/wiki/Collaborative_filtering)
- 📖 [Flask Documentation](https://flask.palletsprojects.com/)
- 📖 [MongoDB Documentation](https://docs.mongodb.com/)
- 📖 [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/index.html)

---

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review the Jupyter Notebook cells for examples
3. Check error messages carefully
4. Review Python/library documentation

---

## License

This project is open-source and available for educational purposes.

---

**Happy Learning! 🎓**

Last Updated: April 2026  
Version: 1.0
