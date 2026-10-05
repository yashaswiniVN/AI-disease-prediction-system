"""AI Based Disease Prediction System - command line version."""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

ADVICE = {
    "Flu": "Take rest, drink fluids, and consult a doctor if needed.",
    "Cold": "Stay warm, drink hot fluids, and take rest.",
    "Dengue": "Drink plenty of fluids and consult a doctor immediately.",
    "Healthy": "You are healthy! Maintain a good lifestyle.",
}

# Load dataset
data = pd.read_csv("disease_data.csv")

# Features and target
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
print("Model Trained Successfully!")

# ---- User Input ----
print("\nEnter symptoms (1 = Yes, 0 = No):")
values = []
for symptom in X.columns:
    label = symptom.replace("_", " ").title()
    while True:
        answer = input(f"{label}: ").strip()
        if answer in ("0", "1"):
            values.append(int(answer))
            break
        print("  Please enter 1 (Yes) or 0 (No).")

# Prediction
user_input = pd.DataFrame([values], columns=X.columns)
prediction = model.predict(user_input)[0]

print("\nPredicted Disease:", prediction)
print("Advice:", ADVICE.get(prediction, "Please consult a doctor."))
print("\nNote: This is not a medical diagnosis. Always consult a doctor.")
