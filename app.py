"""AI Based Disease Prediction System - Streamlit web interface.
Run with:  streamlit run app.py
"""
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier

ADVICE = {
    "Flu": "Take rest, drink fluids, and consult a doctor if needed.",
    "Cold": "Stay warm, drink hot fluids, and take rest.",
    "Dengue": "Drink plenty of fluids and consult a doctor immediately.",
    "Healthy": "You are healthy! Maintain a good lifestyle.",
}

MODELS = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Naive Bayes": BernoulliNB(),
}


@st.cache_data
def load_data():
    return pd.read_csv("disease_data.csv")


st.set_page_config(page_title="AI Disease Prediction", page_icon="🩺")
st.title("🩺 AI Based Disease Prediction System")
st.write("Select the symptoms you are experiencing and click **Predict**.")

data = load_data()
X = data.drop("disease", axis=1)
y = data["disease"]

algo = st.sidebar.selectbox("Choose algorithm", list(MODELS.keys()))
model = MODELS[algo]
model.fit(X, y)

st.subheader("Symptoms")
cols = st.columns(2)
values = []
for i, symptom in enumerate(X.columns):
    label = symptom.replace("_", " ").title()
    choice = cols[i % 2].radio(label, ["No", "Yes"], horizontal=True, key=symptom)
    values.append(1 if choice == "Yes" else 0)

if st.button("Predict"):
    user_input = pd.DataFrame([values], columns=X.columns)
    prediction = model.predict(user_input)[0]
    st.success(f"Predicted Disease: **{prediction}**")
    st.info(f"Advice: {ADVICE.get(prediction, 'Please consult a doctor.')}")
    st.caption("This is not a medical diagnosis. Always consult a doctor.")
