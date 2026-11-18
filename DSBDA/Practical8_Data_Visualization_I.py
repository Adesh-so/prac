
# Practical 8: Data Visualization I
# Titanic Dataset Analysis using Seaborn

# ==========================================
# STEP 1: IMPORT LIBRARIES
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# STEP 2: LOAD BUILT-IN TITANIC DATASET
# ==========================================

df = sns.load_dataset("titanic")

print("First 5 Records:")
display(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Description:")
display(df.describe())

# ==========================================
# STEP 3: CORRELATION MATRIX
# ==========================================

numeric_df = df.select_dtypes(include=["number"])

corr_matrix = numeric_df.corr()

print("\nCorrelation Matrix:")
display(corr_matrix)

plt.figure(figsize=(10, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix of Titanic Dataset")

plt.show()

# ==========================================
# STEP 4: SURVIVAL COUNT BY PASSENGER CLASS
# ==========================================

sns.countplot(
    x='pclass',
    hue='survived',
    data=df
)

plt.title('Survival Count by Passenger Class')

plt.xlabel('Passenger Class')
plt.ylabel('Survival Count')

plt.show()

# ==========================================
# STEP 5: SURVIVAL RATE BY GENDER
# ==========================================

sns.barplot(
    x="sex",
    y="survived",
    data=df,
    errorbar=None
)

plt.title("Survival Rate by Gender")

plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.show()

# ==========================================
# STEP 6: SURVIVAL COUNT BY AGE
# ==========================================

sns.histplot(
    x='age',
    hue='survived',
    data=df,
    multiple="stack"
)

plt.title('Survival Count by Age')

plt.xlabel('Age')
plt.ylabel('Survival Count')

plt.show()

# ==========================================
# STEP 7: SURVIVAL RATE BY EMBARKATION PORT
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x="embarked",
    y="survived",
    data=df,
    hue="embarked",
    palette="coolwarm",
    errorbar=None,
    legend=False
)

plt.title("Survival Rate by Embarkation Port")

plt.xlabel("Port of Embarkation")
plt.ylabel("Survival Rate")

plt.show()

# ==========================================
# STEP 8: FARE DISTRIBUTION FOR SURVIVORS
# ==========================================

sns.boxplot(
    x="survived",
    y="fare",
    data=df,
    hue="survived",
    palette="coolwarm",
    legend=False
)

plt.title("Fare Distribution for Survivors and Non-Survivors")

plt.xlabel("Survival Status (0 = No, 1 = Yes)")
plt.ylabel("Fare Price")

plt.show()

# ==========================================
# STEP 9: SURVIVAL RATE BY DECK
# ==========================================

sns.barplot(
    x="deck",
    y="survived",
    data=df,
    errorbar=None,
    hue="deck",
    palette="coolwarm",
    order=df["deck"].value_counts().index,
    legend=False
)

plt.title("Survival Rate by Deck")

plt.xlabel("Deck")
plt.ylabel("Survival Rate")

plt.show()

# ==========================================
# STEP 10: TICKET FARE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df,
    x="fare",
    hue="pclass",
    bins=30,
    kde=True,
    palette="coolwarm"
)

plt.title("Distribution of Fare by Passenger Class")

plt.xlabel("Fare Price")
plt.ylabel("Number of Passengers")

plt.xlim(0, 300)

plt.show()

# ==========================================
# PRACTICAL 9: AGE DISTRIBUTION BY GENDER
# AND SURVIVAL STATUS
# ==========================================

plt.figure(figsize=(8, 6))

sns.boxplot(
    x="sex",
    y="age",
    hue="survived",
    data=df,
    palette="coolwarm"
)

plt.xlabel("Gender")
plt.ylabel("Age")

plt.title("Age Distribution by Gender and Survival Status")

plt.legend(
    title="Survived",
    labels=["No (0)", "Yes (1)"]
)

plt.show()

# ==========================================
# PRACTICAL COMPLETED
# ==========================================

print("\nPractical 8 and Practical 9 Completed Successfully!")
