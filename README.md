Sentiment Data Analysis Project  
Project Overview:This project focuses on analyzing a sentiment dataset using Python.
The workflow covers the complete data analysis pipeline starting from data cleaning, exploratory analysis, visualization, regression modeling, and time series analysis.The project is divided into two levels (Basic & Intermediate), each including multiple analytical tasks. 
 Level 1 – Basic Analysis
Task 1: Data Cleaning & Preprocessing

Objective: Prepare the raw dataset for analysis.

Steps Performed:

Loaded the dataset using pandas

Removed unnecessary columns (e.g., auto-generated index columns)

Handled missing values

Removed duplicate records

Standardized categorical columns ( Sentiment, Platform, Country)

Converted timestamp column to proper datetime format

Converted numeric columns to correct data types

Saved the cleaned dataset as cleaned_dataset.csv 
Tools Used:Python, pandas
 Task 2: Exploratory Data Analysis (EDA)

Objective: Explore the dataset to understand patterns and summary statistics.

Analysis Included:

Summary statistics (mean, median, standard deviation)

Distribution analysis for numerical features

Correlation analysis between numerical variables

Sentiment distribution overview

Tools Used:Python, pandas, matplotlib, seaborn
  Task 3: Basic Data Visualization

Objective: Visualize relationships and distributions within the dataset.

Visualizations Created:

Histograms (distribution of Likes and Retweets)

Boxplots (outlier detection)

Scatter plots (Likes vs Retweets)

Bar charts (Sentiment distribution)

Line charts (engagement trends over time)

All plots were customized with proper labels, titles, and legends.

Tools Used:matplotlib, seaborn
 Level 2 – Intermediate Analysis
 Task 1: Regression Analysis

Objective: Build a simple Linear Regression model.

Steps Performed:

Selected relevant numerical features

Split dataset into training and testing sets (80/20)

Trained a Linear Regression model using scikit-learn

Evaluated model performance using:

R-squared (R²)

Mean Squared Error (MSE)

Interpreted regression coefficients

Tools Used:Python, pandas, scikit-learn

 Task 2: Time Series Analysis

Objective: Analyze engagement trends over time.

Steps Performed:

Converted timestamp column to datetime

Plotted time-series trends

Applied moving average smoothing

Decomposed the time series into:

Trend

Seasonality

Residuals

Tools Used:Python, pandas, matplotlib, statsmodels

Key Outcomes:

Successfully cleaned and standardized raw data

Extracted insights through EDA and visualization

Built regression models and evaluated performance

Performed time series decomposition and trend analysis.









