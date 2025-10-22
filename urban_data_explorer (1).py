# urban_data_explorer_demo.py
import streamlit as st
import pandas as pd

# -----------------------------
# Function to load a sample of each dataset
# -----------------------------
@st.cache_data
def load_sample_data():
    try:
        landcover = pd.read_excel(
            "LandCoverData.xls", nrows=2000
        )
        population = pd.read_excel(
            "PopulationDensityData.xls", nrows=2000
        )
        realestate = pd.read_excel(
            "RealEstateData.xls", nrows=2000
        )
        transport = pd.read_excel(
            "TransportData.xls", nrows=2000
        )

        # Merge datasets on a common column, e.g., 'city'
        merged_df = (
            landcover.merge(population, on="city", how="outer")
            .merge(realestate, on="city", how="outer")
            .merge(transport, on="city", how="outer")
        )

        return merged_df
    except FileNotFoundError as e:
        st.error(f"Dataset file not found: {e}")
        return pd.DataFrame()  # empty dataframe
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


# -----------------------------
# Streamlit App
# -----------------------------
st.title("Urban Data Explorer (Demo Version)")

data = load_sample_data()

if data.empty:
    st.stop()  # Stop the app if datasets are missing

# Show first few rows
st.subheader("Preview of Dataset (first 10 rows)")
st.write(data.head(10))

# Filters
st.subheader("Filter by City")
if "city" in data.columns:
    selected_cities = st.multiselect(
        "Select cities:", data["city"].unique()
    )
    if selected_cities:
        filtered_data = data[data["city"].isin(selected_cities)]
    else:
        filtered_data = data
else:
    filtered_data = data

# Show filtered data
st.subheader("Filtered Data Preview")
st.write(filtered_data.head(10))

# Summary stats
st.subheader("Summary Statistics (numeric only)")
if not filtered_data.empty:
    st.write(filtered_data.select_dtypes("number").describe())
else:
    st.write("No numeric data available.")

# Download filtered data
st.subheader("Download Filtered Data")
if not filtered_data.empty:
    csv = filtered_data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="filtered_urban_data_demo.csv",
        mime="text/csv",
    )
