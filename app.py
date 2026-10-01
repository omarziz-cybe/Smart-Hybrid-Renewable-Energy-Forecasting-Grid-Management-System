import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="EV Energy Forecast", layout="wide")
st.title("⚡ Smart EV Charging & Renewable Energy Forecasting")

bundle = joblib.load('energy_forecast_xgb.pkl')
results = pd.read_csv('forecasting_test_results.csv')

st.sidebar.header("Control Panel")
days_to_show = st.sidebar.slider("Select the number of days for the offer:", 1, 7, 3)

col1, col2, col3 = st.columns(3)
col1.metric("MAE", f"{bundle['metrics']['mae']:.2f} kW")
col2.metric("RMSE", f"{bundle['metrics']['rmse']:.2f} kW")
col3.metric("R² Score", f"{bundle['metrics']['r2']:.2f}")

st.subheader("Comparing actual load with expected load")
fig, ax = plt.subplots(figsize=(12, 4))
limit = 96 * days_to_show
ax.plot(results['Actual_Load'][:limit], label="Actual", color='gray')
ax.plot(results['Predicted_Load'][:limit], label="Predicted", color='red', linestyle='--')
ax.legend()
st.pyplot(fig)