
# Practical 6: Data Analytics III
# Naive Bayes Classification using Iris Dataset

# ==========================================
# STEP 1: IMPORT LIBRARIES
# ==========================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# STEP 2: LOAD DATASET
# ==========================================

df = pd.read_csv('Practical 6 Iris Naive Bayes.csv')

print("Dataset Information:")
df.info()

print("\nStatistical Description:")
display(df.describe())

# ==========================================
# STEP 3: VISUALIZE OUTLIERS USING BOXPLOTS
# ==========================================

for column in df.columns:

    if df[column].dtype in ['float64', 'int64']:

        plt.figure(figsize=(10, 5))

        sns.boxplot(x=df[column])

        plt.title(f"Box Plot of {column}")
        plt.xlabel(column)

        plt.show()

# ==========================================
# STEP 4: IMPORT MACHINE LEARNING LIBRARIES
# ==========================================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)

# ==========================================
# STEP 5: LABEL ENCODING
# ==========================================

le = LabelEncoder()

df['Species'] = le.fit_transform(df['Species'])

print("\nSpecies Mapping:")

for i, item in enumerate(le.classes_):
    print(f"{item}: {i}")

# ==========================================
# STEP 6: DEFINE FEATURES AND TARGET
# ==========================================

# Remove Id because it is only an identifier
X = df.drop(['Id', 'Species'], axis=1)

# Target variable
y = df['Species']

# ==========================================
# STEP 7: TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=34
)

print("\nTraining and Testing Data Shapes:")

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# ==========================================
# STEP 8: FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# ==========================================
# STEP 9: TRAIN GAUSSIAN NAIVE BAYES MODEL
# ==========================================

model = GaussianNB()

model.fit(X_train_scaled, y_train)

print("\nGaussian Naive Bayes Model Trained Successfully!")

# ==========================================
# STEP 10: MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test_scaled)

print("\nPredicted Values:")
print(y_pred)

# ==========================================
# STEP 11: CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=le.classes_
    )
)

# ==========================================
# STEP 12: CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# ==========================================
# STEP 13: VISUALIZE CONFUSION MATRIX
# ==========================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=le.classes_,
    yticklabels=le.classes_
)

plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.title('Confusion Matrix - Naive Bayes')

plt.show()

# ==========================================
# STEP 14: CALCULATE ACCURACY AND ERROR RATE
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

error_rate = 1 - accuracy

print("\nModel Evaluation:")

print(f"Accuracy: {accuracy:.4f}")

print(f"Error Rate: {error_rate:.4f}")

# ==========================================
# PRACTICAL COMPLETED
# ==========================================

print("\nPractical 6 Completed Successfully!")
