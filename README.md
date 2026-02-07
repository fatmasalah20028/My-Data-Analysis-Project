Sentiment Data Analysis Project
Project Overview

This project focuses on analyzing a Sentiment dataset  using Python.
The workflow covers the complete data analysis pipeline, including:

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Visualization

Regression Modeling

Time Series Analysis

The aim is to extract insights about user sentiment and engagement over time and demonstrate practical data analysis skills on real-world datasets.

Dataset Description

The dataset includes social media entries with post text, sentiment categories, posting times, and user engagement statistics.

Columns include:

Text – Content of the post

Sentiment – Sentiment label (e.g., Positive, Negative, Neutral)

Timestamp – Date and time of the post

User – Username of the poster

Platform – Platform of the post (e.g., Twitter, Instagram)

Hashtags – Associated hashtags

Retweets – Number of retweets/shares

Likes – Number of likes

Country – Country of the user

Year, Month, Day, Hour – Extracted date and time components

Data Cleaning & Preprocessing

Objective: Prepare the raw dataset for analysis.

Steps Performed:

Loaded the dataset using pandas.

Checked for missing values and handled them appropriately.

Checked for duplicate records and removed them.

Removed unnecessary columns (e.g., auto-generated index columns).

Standardized categorical columns: Sentiment, Platform, Country.

Converted Timestamp column to proper datetime format.

Converted numeric columns to correct data types.

Saved the cleaned dataset as cleaned_dataset.csv.

Tools Used: Python, pandas

Exploratory Data Analysis (EDA)

Objective: Explore the dataset to understand patterns, trends, and summary statistics.

Analysis Performed:

Calculated summary statistics: mean, median, mode, standard deviation.

Visualized distributions of numerical features.

Explored correlations between numerical variables.

Examined sentiment distribution and engagement metrics (Likes, Retweets).

Tools Used: Python, pandas, matplotlib, seaborn

Data Visualization

Objective: Visualize relationships and distributions within the dataset.

Visualizations Created:

Histograms: Distribution of Likes and Retweets.

Boxplots: Outlier detection.

Scatter Plots: Likes vs Retweets.

Bar Charts: Sentiment distribution.

Line Charts: Engagement trends over time.

All plots were customized with proper labels, titles, and legends for clarity.

Tools Used: matplotlib, seaborn

Regression Analysis

Objective: Build a simple Linear Regression model to predict engagement metrics.

Steps Performed:

Selected relevant numerical features.

Split the dataset into training and testing sets (80/20).

Trained a Linear Regression model using scikit-learn.

Evaluated model performance using:

R-squared (R²)

Mean Squared Error (MSE)

Interpreted regression coefficients to understand feature impact.

Tools Used: Python, pandas, scikit-learn

Time Series Analysis

Objective: Analyze posting activity and engagement trends over time.

Steps Performed:

Converted Timestamp column to datetime.

Plotted time-series trends.

Applied moving average smoothing to identify trends.

Decomposed the time series into:

Trend

Seasonality

Residuals

Tools Used: Python, pandas, matplotlib, statsmodels

Key Outcomes

Successfully cleaned, checked, and standardized raw data.

Handled missing values and duplicate records.

Extracted insights through EDA and visualization.

Built and evaluated regression models.

Performed time series decomposition and trend analysis.

Tools & Technologies

Python

Pandas

Matplotlib & Seaborn

Scikit-learn

Statsmodels

Conclusion

This project demonstrates practical data analysis skills on real-world Sentiment data, covering the full data analysis pipeline from preprocessing to advanced analytical techniques. It provides a strong foundation for further data science tasks and insights extraction from social media data.

