import joblib
import pandas as pd

pipeline = joblib.load("pipeline_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

FEATURE_COLUMNS = [
    'Country Code', 'Average Cost for two', 'Price range', 'Aggregate rating',
    'Has Table booking', 'Has Online delivery', 'Is delivering now', 'City'
]

def predict_primary_cuisine(input_dict):
    df = pd.DataFrame([input_dict])

    binary_cols = ['Has Table booking', 'Has Online delivery', 'Is delivering now']
    for col in binary_cols:
        df[col] = df[col].astype(int)

    #pred = pipeline.predict(df[FEATURE_COLUMNS])
    #predicted_label = label_encoder.inverse_transform(pred)[0]
    #return predicted_label

    probas = pipeline.predict_proba(df[FEATURE_COLUMNS])
    top3_indices = probas[0].argsort()[::-1][:3]
    top3_labels = label_encoder.inverse_transform(top3_indices)
    print("Top 3 predicted cuisines:", top3_labels)

    return top3_labels.tolist()