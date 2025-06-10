# Cuisine Prediction / Recommendation System
This project is a machine learning-based classification system designed to **predict the primary cuisine(s)** a restaurant is most likely to serve, based on features such as location, services offered, pricing, and user ratings. The app was developed as part of a Machine Learning Internship at **Cognifyz Technologies**.

## Objective
To build a classification model that predicts a restaurant's **likely cuisines** using its attributes like:
- City
- Country code
- Average cost for two
- Price range
- Aggregate rating
- Service features (table booking, delivery, etc.)

## Features
- Predicts **top 3 most likely cuisines** using `predict_proba()` logic
- Fully interactive **Streamlit web app**
- Clean user input interface
- Handles binary and categorical inputs (e.g., Yes/No options)
- Outputs predicted cuisines in real-time

## How to Run
1. Clone the repo or download the files
2. Install dependencies:
```bash
pip install scikit-learn, pandas, streamlit, joblib
```
3. Run the app:
```bash
streamlit run app.py
```