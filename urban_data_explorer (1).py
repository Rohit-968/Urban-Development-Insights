import streamlit as st
import pandas as pd

# -----------------------------
# Dataset URLs
# -----------------------------
LANDCOVER_URL = "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/LandCoverData.xls?download=true"
POPULATION_URL = "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/PopulationDensityData.xls?download=true"
REALESTATE_URL = "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/RealEstateData.xls?download=true"
TRANSPORT_URL = "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/TransportData.xls?download=true"

# -----------------------------
# Function to load sample data from URLs
# -----------------------------
@st.cache_data
def load_sample_data():
    try:
        landcover = pd.read_excel(LANDCOVER_URL, nrows=2000)
        population = pd.read_excel(POPULATION_URL, nrows=2000)
        realestate = pd.read_excel(REALESTATE_URL, nrows=2000)
        transport = pd.read_excel(TRANSPORT_URL, nrows=2000)

        merged_df = (
            landcover.merge(population, on="city", how="outer")
            .merge(realestate, on="city", how="outer")
            .merge(transport, on="city", how="outer")
        )
        return merged_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# -----------------------------
# Streamlit App
# -----------------------------
st.title("Urban Data Explorer (Demo via Hugging Face)")

data = load_sample_data()
if data.empty:
    st.stop()

# Preview
st.subheader("Preview (first 10 rows)")
st.write(data.head(10))

# Filter by city
st.subheader("Filter by City")
if "city" in data.columns:
    selected_cities = st.multiselect("Select cities:", data["city"].unique())
    filtered_data = data[data["city"].isin(selected_cities)] if selected_cities else data
else:
    filtered_data = data

st.subheader("Filtered Data Preview")
st.write(filtered_data.head(10))

# Summary stats
st.subheader("Summary Statistics (numeric only)")
st.write(filtered_data.select_dtypes("number").describe())

# Download filtered data
st.subheader("Download Filtered Data")
csv = filtered_data.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_urban_data_demo.csv",
    mime="text/csv",
)
