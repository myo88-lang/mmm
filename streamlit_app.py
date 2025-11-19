import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# Load your pre-engineered data
df = pd.read_csv('data/man_utd_ml_data.csv')

# Assume your target column is named 'result' or 'Result' (1=Win, 0=Draw, -1=Loss)
target_col = 'Result'  # Change if your column name is different (check your df.columns)

# Features - drop non-numeric or target-related columns
exclude_cols = [target_col, 'Date', 'Opponent', 'Season']  # adjust as needed
feature_cols = [col for col in df.columns if col not in exclude_cols]

X = df[feature_cols]
y = df[target_col]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Best model from testing many (you can also try XGBoost later)
model = RandomForestClassifier(
    n_estimators=500,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    class_weight='balanced'
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, preds):.3f}")
print(classification_report(y_test, preds, target_names=['Loss', 'Draw', 'Win']))

# Save model
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/man_utd_model.pkl')
joblib.dump(feature_cols, 'model/feature_columns.pkl')

print("Model saved as model/man_utd_model.pkl")
print("Features used:", feature_cols)
