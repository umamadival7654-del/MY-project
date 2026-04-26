# Movie Rating Analysis Dashboard - Complete Guide

## Overview
The Movie Rating Analysis application now includes a comprehensive dashboard feature alongside the featured movie editor. The dashboard provides visual analytics, key performance indicators (KPIs), and detailed movie rankings.

## Features

### 🎯 Dashboard View
The main dashboard is the default landing page when you open the application. It includes:

#### 1. **KPI Cards** (Key Performance Indicators)
Four gradient cards displaying critical metrics:
- **Total Movies**: Number of movies in the database
- **Total Ratings**: Total user ratings given
- **Active Users**: Number of unique users
- **Average Rating**: Mean rating across all movies (out of 5.0)

Each card updates automatically when you load the dashboard.

#### 2. **Charts & Visualizations**

##### Rating Distribution Chart
- **Type**: Bar Chart
- **Shows**: How many ratings fall into each rating range (0-1, 1-2, 2-3, 3-4, 4-5)
- **Colors**: Rainbow gradient (Red → Green → Blue)
- **Purpose**: Understand the distribution of user ratings

##### Genre Analysis Chart
- **Type**: Doughnut Chart
- **Shows**: Top 8 genres and their average ratings
- **Colors**: Vibrant gradient colors
- **Purpose**: Identify which genres have the highest average ratings

#### 3. **Top 10 Rated Movies**
Ranked list showing:
- **Rank Badge**: Gold (#1), Silver (#2), Bronze (#3), or standard
- **Movie Title**: Full title of the movie
- **Genres**: Movie genres
- **Rating Count**: Number of ratings received
- **Average Rating**: Stars and numerical rating
- **Interactive**: Hover for highlight effect

#### 4. **Top 10 Most Popular Movies**
Ranked list showing the same information but sorted by:
- **Number of Ratings** (Most Rated)
- Instead of average rating

#### 5. **Statistical Summary**
Four mini cards displaying:
- **Minimum Rating**: Lowest rating value in the dataset
- **Maximum Rating**: Highest rating value in the dataset
- **Std Deviation**: Standard deviation of ratings
- **Avg Ratings/Movie**: Average number of ratings per movie

---

## Navigation

### Tab Navigation
Located below the navbar, provides quick switching between views:

**Dashboard Tab** (📊)
- Shows all analytics and visualizations
- Default landing page
- Auto-loads when page opens

**Featured Movie Tab** (⭐)
- Shows the top-rated single movie
- Allows editing movie features
- See [FEATURE_UPDATE.md](FEATURE_UPDATE.md) for details

Click any tab to switch views instantly.

---

## Dashboard Sections

### Section 1: KPI Cards
```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   Movies    │   Ratings   │    Users    │  Avg Rate   │
│   12,345    │  100,567    │    650      │    3.85     │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### Section 2: Charts
Located side-by-side on wider screens, stacked on mobile:
- **Left**: Rating Distribution (Bar Chart)
- **Right**: Genre Analysis (Doughnut Chart)

### Section 3: Movies Rankings
Two separate sections:
1. **Top Rated**: Movies with highest average ratings
2. **Most Popular**: Movies with most ratings

### Section 4: Statistics
Four metric cards with different color accents:
- 🔵 Minimum Rating
- 🟣 Maximum Rating
- 🟢 Std Deviation
- 🔴 Avg Ratings/Movie

---

## Data Refresh

### Automatic Loading
- Dashboard data loads automatically on page load
- Charts render with animation
- Movie rankings update in parallel

### Manual Refresh
- Click the Dashboard tab to force refresh
- All sections reload with latest data

### Real-time Updates
- Changes made in Featured Movie view update statistics
- New movie edits immediately affect dashboard metrics
- No page reload needed

---

## Responsive Design

### Desktop (1200px+)
- KPI cards: 4 columns
- Charts: 2 columns side-by-side
- Movie lists: Full width

### Tablet (768px - 1199px)
- KPI cards: 2-3 columns
- Charts: Stack vertically
- Movie lists: Full width with adjusted margins

### Mobile (< 768px)
- KPI cards: 2 columns
- Charts: Single column, responsive height
- Movie lists: Full width, optimized for touch
- Navigation tabs: Scrollable if needed

---

## Chart Interactions

### Rating Distribution Chart
- **Hover**: Shows exact count for that rating range
- **Legend**: Click to toggle data series
- **Colors**: Different for each rating range

### Genre Chart
- **Hover**: Shows genre name and rating
- **Legend**: Positioned at bottom, clickable
- **Doughnut Format**: Center is empty for clean look

---

## Data API Endpoints Used

The dashboard pulls data from these backend APIs:

| Endpoint | Purpose | Used For |
|----------|---------|----------|
| `/api/stats` | Get overall statistics | KPI cards, mini stats |
| `/api/ratings/distribution` | Get rating distribution | Rating distribution chart |
| `/api/genres/stats` | Get genre statistics | Genre chart |
| `/api/movies/top-rated` | Get top-rated movies | Top 10 Rated list |
| `/api/movies/popular` | Get popular movies | Top 10 Popular list |

---

## Color Scheme

### KPI Cards
- **Background**: Purple gradient (#667eea → #764ba2)
- **Text**: White
- **Accent**: Light white text for labels

### Rank Badges
- **🥇 Gold**: Top 1 movie (#FFD700)
- **🥈 Silver**: 2nd movie (#C0C0C0)
- **🥉 Bronze**: 3rd movie (#CD7F32)
- **Standard**: Purple gradient (4-10th)

### Chart Colors
- **Bar Chart**: Rainbow (Red, Orange, Yellow, Green, Blue)
- **Doughnut**: Mixed vibrant colors
- **Text**: Dark gray (#333) on white, White on gradient

### Status Badge
- **Connected**: Green (#4CAF50)
- **Error**: Red background
- **Loading**: Gray background

---

## Features Breakdown

### KPI Card Gradient
- Smooth purple gradient background
- Large, readable font size
- Hover effect: Lift up with shadow
- Smooth transitions for updates

### Rank Items
- Circular badge with number
- Movie title (bold, dark)
- Genres and rating count (small, gray)
- Star rating with numerical value (right-aligned)
- Hover: Background highlight
- Touch-friendly on mobile

### Chart Container
- Fixed height: 350px
- Responsive to container width
- Legend integrated
- Smooth animations

### Mini Stats
- Left border color coding
- Label (small, gray)
- Large value display
- 4-column grid, responsive

---

## Performance

### Load Time
- Charts load in parallel for speed
- Lazy rendering of non-visible elements
- Chart.js provides smooth animations

### Data Size
- Dashboard pulls top 10 movies only (not all)
- Genre stats limited to top 8 genres
- Efficient aggregation on backend

### Browser Optimization
- Canvas rendering for charts
- CSS Grid for responsive layout
- Hardware acceleration enabled

---

## Troubleshooting

### Dashboard Not Loading
1. Check if Flask server is running: `python app.py`
2. Verify connection status badge (should show ✓ Connected)
3. Check browser console for errors (F12)
4. Ensure MongoDB is running if required

### Charts Not Displaying
1. Clear browser cache (Ctrl+Shift+Del)
2. Check if Chart.js CDN is accessible
3. Verify `/api/ratings/distribution` endpoint returns data
4. Check browser console for JavaScript errors

### Data Not Updating
1. Click Dashboard tab again to refresh
2. Check if backend API is responding
3. Verify database has sample data loaded
4. Check network tab in DevTools

### Styling Issues
1. Clear CSS cache
2. Hard refresh page (Ctrl+F5)
3. Check if Bootstrap CDN is loading
4. Verify Chart.js CSS is included

---

## Future Enhancements

Potential features for future versions:
- 📅 Date range filtering
- 🔍 Search and filter within top movies
- 📊 Export data as CSV/PDF
- 🎨 Dark mode theme
- 📱 Mobile app version
- 🔔 Real-time notifications
- 🎯 Custom metric selection
- 🌐 Multiple language support

---

## API Reference

### GET /api/stats
**Returns**: Overall statistics
```json
{
  "total_movies": 12345,
  "total_ratings": 100567,
  "total_users": 650,
  "average_rating": 3.85,
  "min_rating": 0.5,
  "max_rating": 5.0,
  "std_rating": 0.95
}
```

### GET /api/movies/top-rated?limit=10
**Returns**: Top-rated movies
```json
{
  "movies": [
    {
      "movieId": 1,
      "title": "Movie Title",
      "genres": "Action|Drama",
      "avg_rating": 4.8,
      "rating_count": 150
    }
  ],
  "count": 10
}
```

### GET /api/genres/stats
**Returns**: Genre statistics
```json
{
  "genres": [
    {
      "_id": "Action",
      "avg_rating": 3.9,
      "total_ratings": 25000
    }
  ],
  "count": 18
}
```

---

## Dashboard Components

### HTML Structure
```
Dashboard View
├── Dashboard Header
├── KPI Grid (4 cards)
├── Chart Grid
│   ├── Rating Distribution Chart
│   └── Genre Chart
├── Top Movies Card
├── Popular Movies Card
└── Stats Summary Card
```

### JavaScript Functions
- `switchView(viewName)` - Switch between views
- `loadDashboard()` - Load all dashboard data
- `loadDashboardStats()` - Load KPI statistics
- `loadRatingDistributionChart()` - Load bar chart
- `loadGenreChart()` - Load doughnut chart
- `loadTopMoviesDashboard()` - Load top movies list
- `loadPopularMoviesDashboard()` - Load popular movies list

---

## CSS Classes

### Container Classes
- `.dashboard-header` - Dashboard title section
- `.kpi-grid` - 4-column responsive grid
- `.chart-grid` - 2-column responsive grid
- `.top-movies-card` - White card container
- `.stats-row` - 4-column stats grid

### Element Classes
- `.kpi-card` - Individual KPI card
- `.kpi-card.gradient` - Gradient KPI card
- `.movie-rank-item` - Movie ranking item
- `.rank-badge` - Rank circle badge
- `.chart-container-full` - Chart canvas container

---

## Keyboard Navigation

- **Tab**: Navigate through elements
- **Enter**: Activate buttons/links
- **Space**: Toggle options
- **Esc**: Close dialogs (if any)

---

## Browser Support

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile Chrome (Android)
- ✅ Mobile Safari (iOS)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Apr 25, 2026 | Initial dashboard release |
| 1.1 | TBD | Add filters and date range |
| 1.2 | TBD | Add export functionality |

---

**Last Updated**: April 25, 2026  
**Status**: Production Ready ✅

For issues or suggestions, check the application logs or contact the development team.
