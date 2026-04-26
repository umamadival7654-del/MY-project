# Movie Rating Analysis - Data Science Project

## 📋 Project Overview

This is a comprehensive end-to-end Data Science project focused on analyzing movie ratings from the MovieLens dataset. The project explores patterns in movie ratings, genre preferences, user behavior, and provides insights for building recommendation systems.

### Problem Statement
Understand movie rating patterns, identify highly-rated movies, analyze genre preferences, and build a simple recommendation system using collaborative filtering to predict user preferences.

### Objectives
1. Load and preprocess MovieLens dataset
2. Perform comprehensive Exploratory Data Analysis (EDA)
3. Identify top-rated and most popular movies
4. Analyze rating distribution across genres
5. Find correlations between movies
6. Build a basic collaborative filtering recommendation system
7. Store analyzed data in MongoDB for persistence
8. Generate actionable insights from the data

---

## 📊 Dataset Details

### MovieLens Dataset
The project uses the MovieLens dataset which contains:

#### **movies.csv**
| Column | Description |
|--------|-------------|
| movieId | Unique identifier for each movie |
| title | Title of the movie |
| genres | Pipe-separated list of genres |

#### **ratings.csv**
| Column | Description |
|--------|-------------|
| userId | Unique identifier for each user |
| movieId | Movie being rated |
| rating | Rating value (0.5 - 5.0 scale) |
| timestamp | Time when rating was given (Unix timestamp) |

---

## 🛠️ Requirements

### Libraries Required
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning algorithms
- **pymongo**: MongoDB integration
- **scipy**: Scientific computing
- **jupyter**: Interactive notebooks

### Installation
```bash
pip install -r requirements.txt
```

### MongoDB Setup
1. Install MongoDB Community Edition
2. Start MongoDB service
3. Create a database: `movie_rating_analysis`
4. MongoDB will auto-create collections when data is inserted

---

## 📁 Project Structure

```
MovieRatingAnalysis/
├── data/
│   ├── movies.csv                 # Movie dataset
│   ├── ratings.csv                # Ratings dataset
│   └── sample_data_generator.py   # Generate sample data
├── notebook/
│   └── movie_analysis.ipynb       # Main analysis notebook
├── src/
│   ├── data_loader.py             # MongoDB integration & data loading
│   ├── recommendation_system.py    # Collaborative filtering
│   └── utils.py                   # Utility functions
├── output/
│   └── (generated visualizations and reports)
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare Data
- Place `movies.csv` and `ratings.csv` in the `data/` folder
- OR use the sample data generator to create test data

### 3. Run MongoDB
```bash
# Windows
mongod

# Linux/Mac
mongod --config /usr/local/etc/mongod.conf
```

### 4. Execute Notebook
```bash
jupyter notebook notebook/movie_analysis.ipynb
```

---

## 📈 Key Features

### 1. Data Preprocessing
- Handle missing values
- Merge datasets
- Data validation
- Genre extraction and processing

### 2. Exploratory Data Analysis
- Statistical summaries
- Distribution analysis
- Outlier detection

### 3. Visualizations
- Top 20 rated movies
- Most popular movies (by rating count)
- Rating distribution histograms
- Genre vs average rating
- Heatmaps for correlations
- Box plots for rating comparisons

### 4. Advanced Analysis
- Genre analysis and trends
- Correlation analysis between movies
- User rating patterns
- Rating time trends

### 5. Recommendation System
- Collaborative filtering (user-based)
- Similarity metrics
- Movie recommendations for users

### 6. MongoDB Integration
- Store analyzed results
- Query data efficiently
- Persist visualizations metadata

---

## 📊 Expected Output

### Key Findings
- Highest-rated movies and their characteristics
- Genre preferences and trends
- Rating patterns and distributions
- Movie similarity networks
- Personalized recommendations

### Visualizations
- Multiple charts and graphs saved to `output/` folder
- Statistical summaries and reports

---

## 🔬 Bonus Features

### Collaborative Filtering Recommendation System
- Item-based and user-based similarity
- Predict movie ratings for users
- Generate top-N recommendations
- Similarity matrix visualization

### MongoDB Integration
- Store user ratings in database
- Query historical data
- Aggregate statistics
- Track analysis metadata

---

## 🎓 Learning Outcomes

After completing this project, you'll understand:
- Data loading and preprocessing techniques
- Exploratory Data Analysis methods
- Data visualization best practices
- Correlation and similarity analysis
- Collaborative filtering basics
- MongoDB CRUD operations
- End-to-end Data Science workflow

---

## 📝 Future Scope

### Enhancements
1. **Advanced Recommendation Systems**
   - Matrix factorization (SVD)
   - Content-based filtering
   - Hybrid approaches

2. **Machine Learning Models**
   - Rating prediction models
   - Genre classification
   - User segmentation

3. **Scalability**
   - Distributed processing with Spark
   - Big data pipeline
   - Real-time recommendations

4. **Web Interface**
   - Flask/Django web app
   - REST API
   - Interactive dashboard

5. **Deep Learning**
   - Neural collaborative filtering
   - RNN for sequential patterns
   - Embedding-based recommendations

---

## 👨‍💻 Code Quality

- ✅ Well-commented code
- ✅ Beginner-friendly
- ✅ Jupyter Notebook format
- ✅ Modular structure
- ✅ Error handling
- ✅ Documentation strings
- ✅ Best practices followed

---

## 🤝 Contributing

Feel free to extend this project with:
- Additional datasets
- New visualizations
- Advanced algorithms
- Performance optimizations

---

## 📚 References

- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Pandas Documentation](https://pandas.pydata.org/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Scikit-learn](https://scikit-learn.org/)

---

## 📄 License

This project is open-source and available for educational purposes.

---

**Created**: April 2026  
**Version**: 1.0  
**Python Version**: 3.8+
