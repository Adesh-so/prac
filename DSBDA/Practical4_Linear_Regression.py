
# Practical 4: Data Analytics I
# Linear Regression for House Price Prediction
# Environment: Anaconda Jupyter Notebook

# ==========================================
# STEP 1: IMPORT LIBRARIES
# ==========================================

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# STEP 2: LOAD DATASET
# ==========================================

df = pd.read_csv('Practical 4 HousingData.csv')

print("First 5 Records:")
display(df.head())

print("\nFirst 26 Records:")
display(df.head(26))

# ==========================================
# STEP 3: DATASET INFORMATION
# ==========================================

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
display(df.describe())

# ==========================================
# STEP 4: CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# STEP 5: HANDLE MISSING VALUES
# ==========================================

cols_with_nan = df.columns[df.isnull().any()].tolist()

for col in cols_with_nan:

    if df[col].dtype in ['float64', 'int64']:

        mean_val = df[col].mean()
        median_val = df[col].median()

        if median_val == 0:
            fill_val = median_val
            strategy = "Median (Zero-dominant)"

        elif abs(mean_val - median_val) > (0.1 * abs(median_val)):
            fill_val = median_val
            strategy = "Median (Skewed)"

        else:
            fill_val = mean_val
            strategy = "Mean (Symmetric)"

        print(f"Filling {col} with {strategy}: {fill_val:.2f}")

        df[col] = df[col].fillna(fill_val)

print("\nMissing Values After Treatment:")
print(df.isnull().sum())

print("\nUpdated Dataset Description:")
display(df.describe())

# ==========================================
# STEP 6: VISUALIZE OUTLIERS USING BOXPLOTS
# ==========================================

for column in df.columns:

    if df[column].dtype in ['float64', 'int64']:

        plt.figure(figsize=(10, 5))

        sns.boxplot(x=df[column])

        plt.title(f"Box Plot of {column}")
        plt.xlabel(column)

        plt.show()

# ==========================================
# STEP 7: TREAT OUTLIERS USING IQR
# ==========================================

for col in df.columns:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lowf = Q1 - 1.5 * IQR
    highf = Q3 + 1.5 * IQR

    df[col] = df[col].clip(
        lower=lowf,
        upper=highf
    )

print("\nOutliers Treated Successfully!")

# ==========================================
# STEP 8: VISUALIZE BOXPLOTS AFTER TREATMENT
# ==========================================

for column in df.columns:

    if df[column].dtype in ['float64', 'int64']:

        plt.figure(figsize=(10, 5))

        sns.boxplot(x=df[column])

        plt.title(f"Box Plot After Outlier Treatment: {column}")
        plt.xlabel(column)

        plt.show()

print("\nDataset After Outlier Treatment:")
display(df.describe())

# ==========================================
# STEP 9: SPLIT DATA INTO FEATURES AND TARGET
# ==========================================

from sklearn.model_selection import train_test_split

# Features (X)
X = df.drop('MEDV', axis=1)

# Target (y)
y = df['MEDV']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining and Testing Data Shapes:")

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# ==========================================
# STEP 10: STANDARDIZATION
# ==========================================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform testing data
X_test_scaled = scaler.transform(X_test)

# Convert arrays back to DataFrames
X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)

print("\nScaled Training Data:")
display(X_train_scaled.head())

print("\nScaled Testing Data:")
display(X_test_scaled.head())

# ==========================================
# STEP 11: TRAIN LINEAR REGRESSION MODEL
# ==========================================

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Train the model
model.fit(X_train_scaled, y_train)

print("\nLinear Regression Model Trained Successfully!")

# ==========================================
# STEP 12: MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test_scaled)

print("\nPredicted House Prices:")
print(y_pred[:10])

# ==========================================
# STEP 13: MODEL EVALUATION
# ==========================================

from sklearn.metrics import mean_squared_error, r2_score

# Calculate MSE
mse = mean_squared_error(y_test, y_pred)

# Calculate RMSE
rmse = np.sqrt(mse)

# Calculate R2 Score
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Results:")

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# ==========================================
# STEP 14: ACTUAL VS PREDICTED VISUALIZATION
# ==========================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=y_test,
    y=y_pred,
    alpha=0.7
)

# Perfect prediction reference line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--',
    lw=2
)

plt.xlabel("Actual MEDV (Home Prices)")
plt.ylabel("Predicted MEDV (Home Prices)")

plt.title("Actual vs Predicted Home Prices (Linear Regression)")

plt.grid(True)

plt.show()

# ==========================================
# PRACTICAL COMPLETED
# ==========================================

print("\nPractical 4 Completed Successfully!")
