<div align="center">

<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--learn-ML%20Modeling-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
<img src="https://img.shields.io/badge/Records-12%2C487-blueviolet?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge"/>

# 🏙️ UrbanLens — Urban Growth Intelligence & Real Estate Analytics

**An end-to-end data science pipeline that decodes where urban value concentrates — and why — by modeling property price drivers across 12,487 records and 24 features. Built for investors, planners, and policy researchers who need answers before the market moves.**

[**Key Findings**](#-key-findings) · [**Methodology**](#-methodology) · [**Model Results**](#-model-performance) · [**Quickstart**](#-quickstart)

---

</div>

## 📌 The Problem

Urban planning and real estate investment live in a paradox: the best decisions are made years before outcomes are visible. By the time a neighborhood's growth is obvious, the opportunity has passed.

**UrbanLens shifts that window.** By learning from historical infrastructure spend, zoning patterns, and socio-economic signals across thousands of records, this system surfaces the leading indicators of urban value creation — before the cranes arrive.

> *Which signals — infrastructure spend, zoning type, socio-economic profile — most reliably predict where urban value will concentrate, and when?*

---

## 🔑 Key Findings

Three findings that directly challenge conventional real estate intuition:

**1. Infrastructure spend precedes price appreciation by years**
Early-stage infrastructure investment is the strongest *leading* indicator of long-term property appreciation. Regions with elevated infrastructure spend in early development phases show disproportionately higher price growth — before any visible development signals appear on the ground.

**2. Mixed-use zoning acts as a price stability buffer**
Mixed-use zones exhibit measurably greater price stability across economic cycles compared to single-use zones. During downturns, single-use residential areas saw sharper corrections; mixed-use corridors retained value significantly better.

**3. Three socio-economic variables outperform visible development signals**
Feature importance analysis identified three socio-economic variables (educational attainment index, employment sector diversity, income mobility score) that consistently predict urban growth trajectories *ahead of* observable construction or planning activity.

---

## 📊 Dataset

| Attribute | Detail |
|---|---|
| Observations | 12,487 records |
| Features | 24 variables |
| Coverage | Property prices, zoning classifications, development timelines, infrastructure spend, socio-economic indicators |
| Source | Public / Open Urban & Real Estate datasets |
| Missing Data Treatment | Context-aware imputation (domain-informed, not median-fill defaults) |
| Outlier Treatment | Reviewed against domain logic — retained where explainable, removed where erroneous |

---

## 🔬 Methodology

### 1 · Data Cleaning & Preprocessing
Missing values were handled with **context-aware imputation** — for example, missing infrastructure spend values in early-development zones were imputed differently from mature zones, rather than applying a blanket statistical fill. Outliers were reviewed case-by-case against domain reasoning: an anomalously high price in a mixed-use zone near a transit hub is not noise — it's signal.

### 2 · Exploratory Data Analysis
- Spatial and temporal pricing trend analysis across development phases
- Correlation heatmaps between infrastructure investment timing and property value trajectories
- Regional development pattern visualization by zoning category
- Distribution analysis of price per square unit across socio-economic strata

### 3 · Feature Engineering

Three derived metrics were constructed to capture dynamics absent from raw features:

| Engineered Feature | What It Captures |
|---|---|
| **Urban Growth Intensity** | Rate of development activity relative to regional baseline — distinguishes fast-rising zones from sustained high-volume ones |
| **Development Velocity** | Speed of change in built environment indicators — a leading signal before price movement is observable |
| **Price per Infrastructure Unit** | Value efficiency of public infrastructure spend — identifies undervalued regions where spend hasn't yet priced in |

### 4 · Predictive Modeling

Multiple regression and ensemble models trained on an 80/20 train-test split with k-fold cross-validation:

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression (baseline) | — | — | 0.61 |
| Random Forest Regressor | — | — | 0.84 |
| Gradient Boosting (XGBoost) | — | — | **0.87** |

> XGBoost outperforms the linear baseline by **+26 points R²**, capturing non-linear interactions between infrastructure timing and socio-economic variables that linear models miss entirely.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Data Wrangling | `pandas` · `numpy` |
| Visualization | `matplotlib` · `seaborn` · `plotly` |
| Modeling | `scikit-learn` · `xgboost` |
| Evaluation | RMSE · MAE · R² · cross-validation |
| Environment | `Python 3.8+` · `Jupyter Notebook` |

---

## 🚀 Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/urbanlens.git
cd urbanlens

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the notebook
jupyter notebook

# 4. Open analysis.ipynb
# Run all cells to reproduce findings, visualizations, and model results end-to-end
```

---

## 📁 Repository Structure

```
urbanlens/
│
├── data/
│   ├── raw/                        # Original unmodified datasets
│   └── processed/                  # Cleaned, engineered, model-ready data
│
├── notebooks/
│   ├── 01_preprocessing.ipynb      # Cleaning, imputation, outlier treatment
│   ├── 02_eda.ipynb                # Exploratory analysis & correlation mapping
│   ├── 03_feature_engineering.ipynb # Derived metric construction
│   └── 04_modeling.ipynb           # Model training, evaluation, feature importance
│
├── src/
│   ├── preprocess.py               # Data cleaning functions
│   ├── features.py                 # Feature engineering pipeline
│   └── model.py                    # Training, evaluation, and prediction logic
│
├── outputs/
│   ├── figures/                    # Exported charts and visualizations
│   └── model_results/              # Saved model artifacts and metrics
│
├── requirements.txt
├── analysis.ipynb                  # Single-notebook end-to-end reproduction
└── README.md
```

---

## 👥 Who This Is For

| Audience | Value Delivered |
|---|---|
| **Real Estate Investors** | Early-signal identification for capital allocation — act before price appreciation is priced in |
| **Urban Planners** | Quantified evidence base for zoning and infrastructure prioritization decisions |
| **Policy Researchers** | Measured relationship between public infrastructure spend and private value creation |
| **Data Science Practitioners** | Reference implementation of domain-informed preprocessing and ensemble modeling on tabular geospatial data |

---

## 🔭 Roadmap

- [ ] Geospatial visualizations with choropleth maps (Folium / GeoPandas)
- [ ] Time-series forecasting for development trend prediction (ARIMA / Prophet)
- [ ] SHAP value analysis for explainable feature importance output
- [ ] Interactive Streamlit dashboard for non-technical stakeholder access
- [ ] Expansion to multi-city datasets for cross-regional generalizability

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built on the conviction that the best investment signal is the one nobody else is looking at yet.**

⭐ Star this repo if it changed how you think about data-driven urban analysis.

</div>
