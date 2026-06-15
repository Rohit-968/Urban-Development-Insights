# Urban Development & Real Estate Insights

**End-to-end data analytics project that identifies high-growth urban regions, models property price drivers, and generates investment-grade insights from 12,487 records across 24 features.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## Key findings

- **Early infrastructure investment** is the strongest leading indicator of long-term property appreciation — regions with early-stage infrastructure spend show disproportionately higher price growth over time
- **Mixed-use zoning** correlates with greater price stability across economic cycles compared to single-use zones
- **Three socio-economic variables** (identified via feature importance) consistently predict urban growth trajectories ahead of visible development signals

---

## Problem

Urban planning and real estate investment operate on decisions made years before outcomes are observable. The core question this project answers:

> *Which signals — infrastructure spend, zoning type, socio-economic profile — most reliably predict where urban value will concentrate, and when?*

---

## Dataset

| Attribute | Detail |
|---|---|
| Source | Public / Open Urban & Real Estate datasets |
| Observations | 12,487 records |
| Features | 24 variables |
| Coverage | Property prices, zoning, development timelines, infrastructure indicators, socio-economic variables |

Raw data was cleaned, validated, and engineered before any modeling — missing values handled with context-aware imputation, outliers reviewed against domain logic rather than removed mechanically.

---

## Methodology

**1. Data cleaning & preprocessing**
Context-aware missing value imputation, outlier treatment grounded in domain logic, feature normalization.

**2. Exploratory data analysis**
Spatial and temporal pricing trend analysis, correlation mapping between infrastructure investment and property value, regional development pattern visualization.

**3. Feature engineering**
Three derived metrics constructed to capture dynamics not present in raw features:

| Feature | Captures |
|---|---|
| Urban growth intensity | Rate of development activity relative to baseline |
| Development velocity | Speed of change in built environment indicators |
| Price per infrastructure unit | Value efficiency of infrastructure spend |

**4. Predictive modeling**
Regression and ensemble ML techniques applied to forecast property prices and rank high-potential regions. Models evaluated on held-out data using RMSE, MAE, and R².

---

## Tech stack

`Python` `Jupyter Notebook` `Pandas` `NumPy` `Matplotlib` `Seaborn` `Scikit-learn`

---

## Setup

```bash
git clone https://github.com/yourusername/urban-development-insights.git
cd urban-development-insights
pip install -r requirements.txt
jupyter notebook
```

Open `analysis.ipynb` to reproduce all findings, visualizations, and model results end-to-end.

---

## Who this is relevant for

- **Urban planners** — evidence base for zoning and infrastructure prioritization
- **Real estate investors** — early-signal identification for capital allocation
- **Policy researchers** — quantified relationship between public spend and private value creation

---

## Roadmap

- [ ] Geospatial visualizations with choropleth maps (Folium / GeoPandas)
- [ ] Time-series forecasting for development trend prediction
- [ ] Interactive dashboard (Streamlit) for non-technical stakeholders

---

## License

MIT — see [LICENSE](LICENSE) for details.
