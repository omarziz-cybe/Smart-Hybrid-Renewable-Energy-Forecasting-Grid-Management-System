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




⚙️ Methodology & PipelineData Ingestion & Alignment:Dynamic batch reading across Excel/CSV sheets using automated timestamp parsing.Entity-relation joins between time-series observations and hardware specifications (ChargerID, GroupID).Feature Engineering:Cyclical Encoding: Captures 24-hour and 12-month periodicity via trigonometric transforms:$$\text{hour\_sin} = \sin\left(\frac{2\pi \cdot \text{hour}}{24}\right), \quad \text{hour\_cos} = \cos\left(\frac{2\pi \cdot \text{hour}}{24}\right)$$Lag Features: Historical consumption offsets ($t-1$, $t-4$ [1 hour], $t-96$ [24 hours]).Rolling Statistics: Moving averages and standard deviations across short-term windows.Model Training & Evaluation:Time-series aware sequential train/test split (80% / 20%).Evaluation metrics:MAE (Mean Absolute Error)RMSE (Root Mean Squared Error)$R^2$ ScoreGrid Overload Simulation:Threshold monitoring identifying potential capacity violations before peak demand occurs.🚀 Getting StartedPrerequisitesMake sure you have Python 3.9+ installed.InstallationClone the repository:
git clone [https://github.com/your-username/smart-energy-forecasting.git](https://github.com/your-username/smart-energy-forecasting.git)
cd smart-energy-forecasting
pip install -r requirements.txt
streamlit run app.py
🛠️ Tech Stack
Languages: Python

Data Manipulation: Pandas, NumPy

Machine Learning: XGBoost, Scikit-learn

Visualization: Matplotlib, Seaborn

Serialization & App: Joblib, Streamlit

📄 License
This project is open-source and available under the MIT License.
---

### How to use it:
1. Create a new file named `README.md` in the main project folder.
2. Paste the content above into it.
3. Edit only the repository link (`your-username`) to match your GitHub account name.
###
