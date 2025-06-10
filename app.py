import streamlit as st
from predictor import predict_primary_cuisine

st.set_page_config(page_title="Cuisine Predictor", layout="centered")
st.title("🍽 Cuisine Predictor App")

st.write("Enter restaurant details to predict the primary cuisine.")

country_code = st.number_input("Country Code", min_value=1, step=1)
city = st.text_input("City")
avg_cost = st.number_input("Average Cost for Two", min_value=0.0, step=10.0)
rating = st.slider("Aggregate Rating", 0.0, 5.0, step=0.1)
price_range = st.selectbox("Price Range (1=Low, 4=High)", [1, 2, 3, 4])
table_booking = st.radio("Has Table Booking?", ['Yes', 'No'])
online_delivery = st.radio("Has Online Delivery?", ['Yes', 'No'])
delivering_now = st.radio("Is Delivering Now?", ['Yes', 'No'])

if st.button("Predict Cuisine"):
    if city.strip() == "":
        st.error("Please enter the city name.")
    else:
        input_dict = {
            'Country Code': country_code,
            'Average Cost for two': avg_cost,
            'Price range': price_range,
            'Aggregate rating': rating,
            'Has Table booking': 1 if table_booking == 'Yes' else 0,
            'Has Online delivery': 1 if online_delivery == 'Yes' else 0,
            'Is delivering now': 1 if delivering_now == 'Yes' else 0,
            'City': city
        }

        try:
            prediction = predict_primary_cuisine(input_dict)
            st.success(f"Predicted Primary Cuisine: 🍽 **{prediction}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
