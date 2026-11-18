
# ==========================================
# PRACTICAL 10: DATA VISUALIZATION III
# IRIS DATASET ANALYSIS
# ==========================================

# STEP 1: IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 2: LOAD IRIS DATASET

df = pd.read_csv('Practical 10 Iris.csv')

print("First 5 Records:")
display(df.head())

print("\nDataset Information:")
df.info()

# STEP 3: IDENTIFY FEATURES AND DATA TYPES

print("\nFeatures and their Data Types:")
display(df.dtypes)

print("\nNumber of Rows and Columns:")
print(df.shape)

# Exclude Id because it is only an identifier
numerical_features = [
    'SepalLengthCm',
    'SepalWidthCm',
    'PetalLengthCm',
    'PetalWidthCm'
]

categorical_features = ['Species']

print("\nNumerical Features:", numerical_features)
print("Number of Numerical Features:", len(numerical_features))

print("\nCategorical Features:", categorical_features)
print("Number of Categorical Features:", len(categorical_features))

print("\nTotal Relevant Features:", 
      len(numerical_features) + len(categorical_features))

# STEP 4: HISTOGRAMS FOR NUMERICAL FEATURES

plt.figure(figsize=(15, 10))

for i, feature in enumerate(numerical_features):
    plt.subplot(2, 2, i + 1)

    sns.histplot(df[feature], bins=15, kde=True)

    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# STEP 5: BOXPLOTS FOR NUMERICAL FEATURES

plt.figure(figsize=(15, 10))

for i, feature in enumerate(numerical_features):
    plt.subplot(2, 2, i + 1)

    sns.boxplot(y=df[feature])

    plt.title(f'Boxplot of {feature}')
    plt.ylabel(feature)

plt.tight_layout()
plt.show()

# STEP 6: OUTLIER DETECTION USING IQR METHOD

def find_outliers_iqr(series):

    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = series[
        (series < lower_bound) | (series > upper_bound)
    ]

    return outliers, Q1, Q3, IQR, lower_bound, upper_bound


print("\nOUTLIER ANALYSIS USING IQR METHOD")

for feature in numerical_features:

    outliers, Q1, Q3, IQR, lower_bound, upper_bound = find_outliers_iqr(
        df[feature]
    )

    print("\nFeature:", feature)
    print("Q1:", round(Q1, 2))
    print("Q3:", round(Q3, 2))
    print("IQR:", round(IQR, 2))
    print("Lower Bound:", round(lower_bound, 2))
    print("Upper Bound:", round(upper_bound, 2))

    if not outliers.empty:

        print("Number of Outliers:", len(outliers))

        print("Outlier Records:")
        display(df.loc[outliers.index])

    else:

        print("No Outliers Detected")

# STEP 7: SPECIES-WISE BOXPLOT OF PETAL WIDTH

plt.figure(figsize=(10, 6))

sns.boxplot(
    x='Species',
    y='PetalWidthCm',
    data=df
)

plt.title('Species-wise Boxplot of PetalWidthCm')
plt.xlabel('Species')
plt.ylabel('PetalWidthCm')

plt.show()

# STEP 8: SPECIES-WISE HISTOGRAMS OF PETAL WIDTH

plt.figure(figsize=(15, 5))

for i, species in enumerate(df['Species'].unique()):

    species_data = df[df['Species'] == species]

    plt.subplot(1, 3, i + 1)

    sns.histplot(
        species_data['PetalWidthCm'],
        bins=10,
        kde=True
    )

    plt.title(f'Histogram of PetalWidthCm for {species}')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# STEP 9: SPECIES-WISE OUTLIER DETECTION

print("\nOUTLIERS FOR PETAL WIDTH PER SPECIES")

for species in df['Species'].unique():

    species_data = df[
        df['Species'] == species
    ]['PetalWidthCm']

    outliers, Q1, Q3, IQR, lower_bound, upper_bound = find_outliers_iqr(
        species_data
    )

    print("\nSpecies:", species)

    if not outliers.empty:

        print("Number of Outliers:", len(outliers))

        print("Outlier Records:")
        display(df.loc[outliers.index])

    else:

        print("No Outliers Detected")

# STEP 10: PRACTICAL COMPLETED

print("\nPractical 10 Completed Successfully!")
