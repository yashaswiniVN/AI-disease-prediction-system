# 🩺 AI Based Disease Prediction System

A mini project that uses machine learning to predict the most probable disease from symptoms entered by the user, and gives basic health advice.

**Author:** Yashaswini V N

**Institution:** GRT Institute of Engineering and Technology

**Mini Project**

> ⚠️ **Disclaimer:** This project is for educational purposes only. It is not a medical diagnosis tool. Always consult a qualified doctor.

## Abstract
Artificial Intelligence is transforming healthcare by enabling faster and more accurate disease prediction. This system analyzes user-provided symptoms using machine learning algorithms and predicts the most probable disease along with basic recommendations, improving accessibility to early medical guidance.

## Objectives
- Develop an AI-based disease prediction system
- Analyze symptoms and predict diseases
- Improve early diagnosis and reduce decision time
- Assist doctors with data-driven insights
- Provide basic healthcare suggestions and increase accessibility

## Tools & Technologies
- Python
- Pandas, NumPy, Scikit-learn
- Streamlit (web interface)
- Algorithms: Decision Tree, Random Forest, Naive Bayes

## Project Structure
```
ai-disease-prediction-system/
├── app.py                  # Streamlit web interface
├── disease_prediction.py   # Command-line version
├── disease_data.csv        # Symptom–disease dataset
├── requirements.txt        # Python dependencies
├── README.md
├── LICENSE
└── .gitignore
```

## Methodology
1. **Data Collection** – symptom/disease dataset (`disease_data.csv`)
2. **Data Preprocessing** – clean data; symptoms encoded as 0/1
3. **Feature Selection** – symptoms are inputs, disease is the output
4. **Model Training** – Decision Tree, Random Forest, Naive Bayes
5. **User Input** – Yes/No symptom selection
6. **Prediction** – model predicts the most probable disease
7. **Result & Suggestion** – predicted disease with basic advice
8. **Output Display** – shown through Streamlit interface

## Installation
```bash
git clone https://github.com/<your-username>/ai-disease-prediction-system.git
cd ai-disease-prediction-system
pip install -r requirements.txt
```

## Usage

**Command-line version**
```bash
python disease_prediction.py
```

**Web interface (Streamlit)**
```bash
streamlit run app.py
```

## Sample Output
```
Model Trained Successfully!

Enter symptoms (1 = Yes, 0 = No):
Fever: 1
Cough: 0
Headache: 1
Fatigue: 1
Body Pain: 1
Nausea: 1

Predicted Disease: Dengue
Advice: Drink plenty of fluids and consult a doctor immediately.
```

## Challenges
- Collecting accurate medical datasets
- Handling missing or incorrect data
- Avoiding wrong predictions
- Limited real-time medical validation

## Limitations
- Small sample dataset; accuracy depends on dataset quality
- Basic security features
- Needs expert verification before any real-world use

## Future Improvements
- Integration with mobile applications
- Real-time doctor consultation
- Deep learning for better accuracy
- Multi-language support and advanced prediction using medical reports

## References
1. Python Documentation – https://docs.python.org
2. Pandas Documentation – https://pandas.pydata.org
3. Kaggle (medical datasets) – https://www.kaggle.com
4. "AI in Medical Diagnosis" – PubMed articles
5. "Artificial Intelligence in Healthcare: Past, Present and Future" – IEEE Xplore

## License
Released under the MIT License.
