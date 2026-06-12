import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load feature dataset
df = pd.read_csv(r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\data\processed\ml_dataset_v3.csv")

# Features (X)
X = df[
    [
        "team1_win_rate",
        "team2_win_rate",
        "team1_recent_form",
        "team2_recent_form",
        "head_to_head_advantage",
        "toss_advantage"
    ]
]
# Target (y)
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nMODEL RESULTS")
print("-" * 40)

print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(
    feature_importance.sort_values(
        by="Importance",
        ascending=False
    )
)

import joblib

joblib.dump(model, r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\model\ipl_predictor.pkl")

print("\nModel saved successfully!")
