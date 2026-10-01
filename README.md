# ⚡ Smart Hybrid Renewable Energy & EV Load Forecasting

An end-to-end Machine Learning pipeline designed to forecast Electric Vehicle (EV) charging demand and integrate smart load predictions with renewable energy capacity constraints.

---

## 📌 Project Overview
As the penetration of electric vehicles increases, charging infrastructure places substantial peaks on electrical grids. This project provides a robust time-series forecasting solution that models dynamic charging behavior, temporal seasonality, and spatial charger configurations to predict energy consumption and prevent grid overload.

### Key Objectives:
- **Consolidation**: Automated ingestion and merging of multi-resolution time-series data (15-minute intervals) with metadata (Charger Installations, Group Definitions, and Capacity Profiles).
- **Feature Engineering**: Integration of cyclical temporal encodings ($\sin/\cos$), lag features, and rolling-window statistical aggregates.
- **Forecasting Engine**: Optimized Gradient Boosting Regressor (**XGBoost**) capturing non-linear demand trends.
- **Grid Safety & Monitoring**: Automated alerting pipeline detecting load exceedance against network capacity thresholds.

---

## 📂 Repository Structure

```text
├── data/
│   ├── GreenFlux15Minute/          # Raw 15-minute time-series logs
│   ├── ChargerInstall.xlsx         # Charger specifications & installation data
│   ├── CapacityProfile.xlsx        # Grid capacity limits and constraints
│   ├── GroupDefinition.xlsx        # Group and cluster mappings
│   └── GreenFlux Transactions.xlsx # Charging transaction sessions
├── models/
│   └── energy_forecast_xgb.pkl     # Exported model bundle (model, features, metrics)
├── notebooks/
│   └── energy_forecasting.ipynb    # Complete analysis and training pipeline
├── app.py                          # Streamlit interactive forecasting dashboard
├── forecasting_test_results.csv    # Evaluated inference output
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
