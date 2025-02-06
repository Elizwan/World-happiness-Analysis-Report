#!/usr/bin/env python
# coding: utf-8

# # EXPLORATORY DATA ANALYSIS FOR WORLD HAPPINESS REPORT

# # 1. Introduction

# The World Happiness Report is a global ranking of countries based on their citizens' happiness. This project aims to explore and visualize the factors contributing to happiness across the world.

# # 1.1 Importing libraries

# The first step of the process is importing the libraries needed to run our analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # 1.2 Load the Dataset

# We then the load the dataset that we are going to use for our analysis.We also display the first five rows and columns of the dataset to ensure we are in the correct dataset.

# In[3]:


#loading the dataset
df=pd.read_csv("D:\chrome\world-happiness-2019.csv")


# In[4]:


# Display the first five rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())


# In[5]:


# Check the column names
print("\nColumn names in the dataset:")
print(df.columns)


# # 2. Data Cleaning

# We check for any missing values or duplicate rows.

# In[6]:


# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

# Display summary of cleaned data
df.info()


# # 3. Summary Statistics

# We check for descriptive statistics of the dataset

# In[7]:


# Summary statistics
print(df.describe())


# # 4. Data Visualization

# We now visualize the top 10 happiest countries using a bar plot, correlation heatmap,and happiness distribution

# # 4.1 Top 10 Happiest Countries Based on World Happiness Scores
# 

# In[19]:


# Top 10 happiest countries using a bar chart
top_10_happiness = df[['Score', 'Country or region']].sort_values(by='Score', ascending=False).head(10)

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Score', y='Country or region', data=top_10_happiness, palette="YlGnBu")

# Labeling the axes and the plot
plt.xlabel('Happiness Score')  
plt.ylabel('Country') 
plt.title('Top 10 Happiest Countries in 2019') 
plt.xticks(rotation=45, ha="right") 

# Display the plot
plt.show()



# # 4.2 Correlation Heatmap

# In[21]:


# Select only the numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Create a correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Happiness Factors')
plt.show()


# # 4.3 Happiness score distribution
# 

# In[24]:


# Happiness score distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Score'], kde=True, bins=20, color='purple')
plt.title('Distribution of Happiness Scores')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.show()


# # 5. Analysis and Insights

# The happiest country from the 158 countries analysed is Finland.

# The data shows that countries with higher GDP per Capita,healthy life expectancy have higher happiness scores

# There is a strong positive correlation between GDP per Capita,healthy life expectancy,social support and happiness scores.GDP per capita is the factor that is the most strongly correlated with the happiness scores, with a correlation coefficient of 0.79. This suggests wealth and economic prosperity can contribute to a higher standard of living, which can lead to greater happiness.

# There is a weak correlation between Generosity and happiness scores, with a correlation coefficient of 0.08, suggesting that a country's level of generosity does not contribute to happiness

# # 6. Conclusion

# The data revealed a clear correlation between a country's GDP per capita and its happiness score, which suggests that economic prosperity plays a significant role in the overall well-being of a nation's citizens

# The top-ranked countries, including Finland, Denmark, and Norway, share several common characteristics, their geographical location contributes to their happiness as well.

# In conclusion, this analysis reinforces the idea that economic stability, strong social support systems, and a healthy environment contribute significantly to the happiness of a nation's citizens. Policymakers should focus on improving these aspects to enhance well-being and overall life satisfaction in their respective countries.

# In[ ]:




