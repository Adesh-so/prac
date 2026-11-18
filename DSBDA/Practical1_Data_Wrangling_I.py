
# Practical 1: Data Wrangling I
# Dataset: Titanic Dataset
# Environment: Anaconda Jupyter Notebook

# 1. Import Required Libraries
import pandas as pd
import numpy as np

# 2. Load Dataset
df = pd.read_csv('Titanic-Dataset.csv')

display(df.head(10))

# 3. Statistical Description
print("Statistical Description:")
display(df.describe())

# 4. Dataset Information
print("Dataset Information:")
df.info()

# 5. Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Dataset Description and Source
# Source: Kaggle - Titanic Machine Learning from Disaster
# Description:
# The Titanic dataset contains passenger information such as
# age, gender, passenger class, fare and survival status.

# 7. Check Dimensions of DataFrame
print("\nDimensions of DataFrame:", df.shape)

# Variable Descriptions:
# PassengerId: Unique passenger ID
# Survived: Survival status (0 = No, 1 = Yes)
# Pclass: Passenger class
# Name: Passenger name
# Sex: Gender
# Age: Passenger age
# SibSp: Siblings/spouses aboard
# Parch: Parents/children aboard
# Ticket: Ticket number
# Fare: Ticket fare
# Cabin: Cabin number
# Embarked: Port of embarkation

# 8. Data Formatting and Missing Value Handling
print("\nCurrent Data Types:")
print(df.dtypes)

# Convert Embarked into category
df['Embarked'] = df['Embarked'].astype('category')

# Fill missing Age values using median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked values using mode
df['Embarked'] = df['Embarked'].cat.add_categories(['Unknown']).fillna('Unknown')

# Drop Cabin column
df.drop(columns=['Cabin'], inplace=True)

print("\nUpdated Data Types:")
print(df.dtypes)

# 9. Convert Categorical Variables into Numerical Variables

# Label Encoding for Sex
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-Hot Encoding for Embarked
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print("\nDataFrame After Encoding:")
display(df.head())

# 10. Check Updated DataFrame
print("\nUpdated DataFrame Information:")
df.info()

print("\nUpdated Statistical Description:")
display(df.describe())

# 11. Data Normalization using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

print("\nData After Min-Max Normalization:")
display(df[['Age', 'Fare']].head())

# 12. Data Standardization using StandardScaler
from sklearn.preprocessing import StandardScaler

# Load original dataset for independent standardization
df_standardized = pd.read_csv('Titanic-Dataset.csv')

# Handle missing values
df_standardized['Age'] = df_standardized['Age'].fillna(
    df_standardized['Age'].median()
)

df_standardized['Fare'] = df_standardized['Fare'].fillna(
    df_standardized['Fare'].median()
)

std_scaler = StandardScaler()

df_standardized[['Age', 'Fare']] = std_scaler.fit_transform(
    df_standardized[['Age', 'Fare']]
)

print("\nData After Standardization:")
display(df_standardized[['Age', 'Fare']].describe().round(4))

# Practical 1 Completed Successfully
