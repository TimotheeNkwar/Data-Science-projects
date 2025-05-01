##  project 1

### 🧠 **Laptop EDA with Python – Project Summary**

This project involves **Exploratory Data Analysis (EDA)** on a dataset of laptops to uncover insights about **price, performance, brand trends, and hardware configurations**. Using Python libraries like **Pandas, Matplotlib, Seaborn**, and **Plotly**, the project explores key features such as:

- **Processor type, RAM, and storage**
- **Display size and resolution**
- **Brand-wise pricing**
- **Correlation between features and price**

The goal is to understand **what factors influence laptop prices**, detect **outliers or trends**, and prepare the dataset for further modeling (e.g. price prediction). It’s a great example of applying **data cleaning, visualization, and feature engineering** on real-world tech product data.

## project 2

### 🧠 **Predicting Gender Based on Features – Project Summary**

This project involves building a **machine learning model** to predict a person's **gender** based on features such as **height, weight, Age**, and other biometric traits. The dataset was preprocessed, analyzed, and used to train classification models in Python.

#### ✅ Key steps:
- **Data cleaning & preprocessing** with `Pandas` and `Scikit-learn`
- **EDA** using `Seaborn` and `Matplotlib` to visualize feature distributions by gender
- **Feature selection** based on correlation with the target variable
- **Model training** with algorithms like:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
#### 🎯 Results:
- The best model achieved an **accuracy of ~89%** on the test set with the knn algorithm.
- Important features: **height**, **weight**, and **foot size**
- The model was evaluated using a **confusion matrix**, **precision**, and **recall**

## project 3
### 🧠 Outlier Detection & Removal – IQR (InterQuartile Range) Method

A data cleaning project aimed at detecting and removing outliers from a dataset using the IQR method.  
This technique identifies extreme values based on the interquartile range and eliminates them to improve data quality.

- Calculated Q1 and Q3 to find the IQR (Q3 − Q1)
- Identified outliers outside the range \[Q1 − 1.5×IQR, Q3 + 1.5×IQR\]
- Removed outliers to obtain a cleaner dataset
- Applied on real or simulated data with optional visualization (e.g., boxplot)

## project 4
### 🧠 EDA on Crime in the USA

Project focused on performing **Exploratory Data Analysis (EDA)** to understand patterns and trends in crime across the United States.  
The analysis includes exploring the relationships between crime rates and socio-economic factors, regional differences, and trends over time.

- Loaded and preprocessed the **crime dataset** (e.g., from FBI or open data sources)
- Analyzed crime rate distributions using **histograms** and **box plots**
- Investigated correlations between crime rates and socio-economic factors (e.g., unemployment, poverty)
- Visualized geographic crime patterns using **heatmaps** and **scatter plots**
- Analyzed crime trends over time and by region

> 🔧 Tools used: Python, Pandas, Matplotlib, Seaborn


