
# Practical 3: Descriptive Statistics
# Measures of Central Tendency and Variability
# Environment: Anaconda Jupyter Notebook

# ==========================================
# PART 1: ADULT DATASET
# ==========================================

# Step 1: Import Required Libraries

import pandas as pd
import numpy as np
import seaborn as sns

# Step 2: Load Adult Dataset

df = pd.read_csv('Practical 3.1 adult.csv')

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("First Five Records:")
display(df.head())

# Step 3: Display Dataset Information

print("\nDataset Information:")
df.info()

# Step 4: Check Dataset Dimensions

print("\nDataset Shape:")
print(df.shape)

# Step 5: Group Age by Workclass

print("\nAge Statistics Grouped by Workclass:")
display(df.groupby('Workclass')['Age'].describe())

# Step 6: Summary Statistics Grouped by Education

summary_stats = df.groupby('Education')['Age'].agg(
    ['mean', 'median', 'min', 'max', 'std']
)

print("\nSummary Statistics of Age Grouped by Education:")
display(summary_stats)

# Step 7: Convert Categorical Education into Numeric Values

df['Education_Numeric'], category_list = pd.factorize(
    df['Education']
)

print("\nNumeric Mapping for Education Categories:")
display(df[['Education', 'Education_Numeric']].head(10))

# Step 8: Display Unique Category Mapping

mapping_df = pd.DataFrame({
    'Category': category_list,
    'Numeric_Value': range(len(category_list))
})

print("\nUnique Mapping List:")
display(mapping_df)

# Step 9: Alternative Method Using LabelEncoder

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Education_LabelEncoded'] = le.fit_transform(
    df['Education']
)

le_summary = df.groupby('Education')['Age'].agg(
    ['mean', 'median', 'min', 'max', 'std']
)

print("\nSummary Statistics Using LabelEncoder:")
display(le_summary)

# Display LabelEncoder Mapping

le_mapping = pd.DataFrame({
    'Category': le.classes_,
    'Numeric_Value': range(len(le.classes_))
})

print("\nLabelEncoder Mapping:")
display(le_mapping)


# ==========================================
# PART 2: IRIS DATASET
# ==========================================

# Step 10: Load Iris Dataset

iris = sns.load_dataset('iris')

print("\nFirst Five Records of Iris Dataset:")
display(iris.head())

# Step 11: Display Iris Dataset Information

print("\nIris Dataset Information:")
iris.info()

# Step 12: Filter Three Species

species_list = [
    'setosa',
    'versicolor',
    'virginica'
]

# Step 13: Display Statistical Details

for species in species_list:

    print(
        f"\n--- Statistical Details for "
        f"{species.capitalize()} ---"
    )

    stats = iris[
        iris['species'] == species
    ].describe(
        percentiles=[0.25, 0.50, 0.75]
    )

    display(stats)


# Practical 3 Completed Successfully
