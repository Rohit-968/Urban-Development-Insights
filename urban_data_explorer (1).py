# urban_data_explorer_safe.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Urban Data Explorer", layout="wide")
st.title("Urban Data Explorer (Memory Efficient & Safe)")

# -----------------------------
# Load datasets safely
# -----------------------------
@st.cache_data
def load_data(nrows=100000):
    try:
        # Load only a subset to save memory
        landcover = pd.read_csv("LandcoverData.csv", nrows=nrows)
        population = pd.read_csv("PopulationData.csv", nrows=nrows)
        realestate = pd.read_csv("RealEstateData.csv", nrows=nrows)
        transport = pd.read_csv("TransportData.csv", nrows=nrows)

        merged_df = landcover.merge(population, on='city', how='outer') \
                             .merge(realestate, on='city', how='outer') \
                             .merge(transport, on='city', how='outer')
        return merged_df
    except FileNotFoundError as e:
        st.error(f"Dataset file not found: {e}")
        return pd.DataFrame()  # empty df to prevent crashes

data = load_data()

if data.empty:
    st.warning("No data loaded. Please make sure the CSV files are in the same folder as this script.")
    st.stop()

# -----------------------------
# Filtering options
# -----------------------------
st.subheader("Filter Data")
merge_keys = [col for col in data.columns if col.lower() in ['city', 'region', 'area', 'district', 'id']]

if merge_keys:
    selected_key = st.selectbox("Filter by:", merge_keys)
    if selected_key:
        unique_values = data[selected_key].dropna().unique()
        selected_values = st.multiselect(f"Select {selected_key}:", unique_values)
        filtered_data = data[data[selected_key].isin(selected_values)] if selected_values else data
else:
    filtered_data = data

# -----------------------------
# Show limited rows only
# -----------------------------
st.write(f"Showing first 1000 rows of {len(filtered_data)} filtered rows:")
if not filtered_data.empty:
    st.dataframe(filtered_data.head(1000))
else:
    st.info("No data matches the selected filter.")

# -----------------------------
# Summary stats
# -----------------------------
st.subheader("Summary Statistics (numeric only to save memory)")
if not filtered_data.empty and filtered_data.select_dtypes(include='number').shape[1] > 0:
    st.write(filtered_data.describe())
else:
    st.info("No numeric columns to describe.")

# -----------------------------
# Download filtered data
# -----------------------------
st.subheader("Download Filtered Data")
if not filtered_data.empty:
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="filtered_urban_data.csv",
        mime="text/csv"
    )
else:
    st.info("No data to download.")
