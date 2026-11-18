
# Practical 2: Data Cleaning and Data Transformation
# Environment: Anaconda Jupyter Notebook

# Step 1: Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Creating a Synthetic Dataset

data = {
    'RollNo': range(1, 31),
    'Name': [f'Student_{i}' for i in range(1, 31)],
    'Gender': np.random.choice(['M', 'F'], 30),

    'Math_Score': [
        85, 90, np.nan, 70, 60, 150, 45, 88, 92, 78,
        82, 10, 95, 89, 77, 84, 91, 65, 72, 80,
        55, 120, 88, 94, 76, 83, 87, 90, 40, 85
    ],

    'Science_Score': np.random.randint(50, 100, 30),

    'Attendance': [
        95, 80, 85, 10, 100, 75, 88, 92, 70, 85,
        90, 82, 88, 94, 76, 83, 87, 90, 40, 85,
        95, 80, 85, 10, 100, 75, 88, 92, 70, 85
    ]
}

df = pd.DataFrame(data)

# Adding Intentional Missing Values

df.loc[5, 'Science_Score'] = np.nan
df.loc[10, 'Attendance'] = np.nan

print("Initial Dataset Preview:")
display(df.head(10))

print("\nSummary Statistics:")
display(df.describe())


# Step 2: Handling Missing Values and Inconsistencies

print("\nMissing Values Per Column:")
print(df.isnull().sum())

# Fill Math_Score with Median
df['Math_Score'] = df['Math_Score'].fillna(
    df['Math_Score'].median()
)

# Fill Science_Score with Median
df['Science_Score'] = df['Science_Score'].fillna(
    df['Science_Score'].median()
)

# Fill Attendance with Mean
df['Attendance'] = df['Attendance'].fillna(
    df['Attendance'].mean()
)

print("\nMissing Values After Treatment:")
print(df.isnull().sum())


# Step 3: Outlier Detection and Treatment

# Visualizing Outliers Using Boxplot

plt.figure(figsize=(10, 5))

sns.boxplot(
    data=df[['Math_Score', 'Science_Score', 'Attendance']]
)

plt.title('Detection of Outliers')
plt.show()

# Treating Outliers in Math_Score Using IQR

Q1 = df['Math_Score'].quantile(0.25)
Q3 = df['Math_Score'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Clipping Outliers to Bounds

df['Math_Score'] = np.where(
    df['Math_Score'] > upper_bound,
    upper_bound,
    np.where(
        df['Math_Score'] < lower_bound,
        lower_bound,
        df['Math_Score']
    )
)

print(
    f"Outliers handled. Math_Score range clipped to "
    f"{lower_bound} - {upper_bound}"
)


# Step 4: Data Transformation

print(
    f"\nSkewness Before Transformation: "
    f"{df['Attendance'].skew()}"
)

# Applying Log Transformation

df['Log_Attendance'] = np.log1p(df['Attendance'])

# Visualizing Distribution Change

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(
    df['Attendance'],
    kde=True,
    ax=axes[0]
)

axes[0].set_title('Original Attendance')

sns.histplot(
    df['Log_Attendance'],
    kde=True,
    ax=axes[1]
)

axes[1].set_title('Log Transformed Attendance')

plt.tight_layout()
plt.show()

print(
    f"Skewness After Transformation: "
    f"{df['Log_Attendance'].skew()}"
)


# Step 5: Display Final Dataset

print("\nFinal Dataset:")
display(df.head(10))

print("\nFinal Dataset Information:")
df.info()

print("\nFinal Summary Statistics:")
display(df.describe())


# Practical 2 Completed Successfully
