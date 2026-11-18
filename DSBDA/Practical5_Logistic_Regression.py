
# Practical 5: Data Analytics II
# Logistic Regression using Social Network Ads Dataset

# ==========================================
# STEP 1: IMPORT LIBRARIES
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# STEP 2: LOAD DATASET
# ==========================================

df = pd.read_csv('Practical 5 Social_Network_Ads.csv')

print("DataFrame Head:")
display(df.head())

print("\nDataFrame Description:")
display(df.describe())

print("\nDataFrame Information:")
df.info()

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
# STEP 4: DATA PREPROCESSING
# ==========================================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# Remove User ID because it is not useful for prediction
df_processed = df.drop('User ID', axis=1)

# Convert Gender into numerical values
le = LabelEncoder()

df_processed['Gender'] = le.fit_transform(
    df_processed['Gender']
)

print("\nGender Mapping:")

for i, item in enumerate(le.classes_):
    print(f"{item}: {i}")

# ==========================================
# STEP 5: DEFINE FEATURES AND TARGET
# ==========================================

X = df_processed[['Gender', 'Age', 'EstimatedSalary']]

y = df_processed['Purchased']

# ==========================================
# STEP 6: TRAIN-TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining and Testing Data Shapes:")

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)

print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# ==========================================
# STEP 7: FEATURE SCALING
# ==========================================

scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform testing data
X_test_scaled = scaler.transform(X_test)

# ==========================================
# STEP 8: TRAIN LOGISTIC REGRESSION MODEL
# ==========================================

classifier = LogisticRegression(random_state=42)

classifier.fit(X_train_scaled, y_train)

print("\nLogistic Regression Model Trained Successfully!")

# ==========================================
# STEP 9: MAKE PREDICTIONS
# ==========================================

y_pred = classifier.predict(X_test_scaled)

print("\nPredicted Values:")
print(y_pred)

# ==========================================
# STEP 10: MODEL EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

error_rate = 1 - accuracy

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

print("\nModel Evaluation Results:")

print(f"Accuracy: {accuracy:.4f}")
print(f"Error Rate: {error_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# ==========================================
# STEP 11: CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Extract TP, TN, FP, FN
TN, FP, FN, TP = cm.ravel()

print("\nConfusion Matrix Values:")

print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)

# ==========================================
# STEP 12: CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(classification_report(y_test, y_pred))

# ==========================================
# STEP 13: VISUALIZE CONFUSION MATRIX
# ==========================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Predicted No Purchase', 'Predicted Purchase'],
    yticklabels=['Actual No Purchase', 'Actual Purchase']
)

plt.title('Confusion Matrix for Logistic Regression')

plt.xlabel('Predicted Label')
plt.ylabel('True Label')

plt.show()

# ==========================================
# PRACTICAL COMPLETED
# ==========================================

print("\nPractical 5 Completed Successfully!")
