import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    data_files = {
        "landcover": "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/LandCoverData.xls",
        "population": "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/PopulationDensityData.xls",
        "realestate": "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/RealEstateData.xls",
        "transport": "https://huggingface.co/datasets/Rxyz21/UrbanInsight/resolve/main/TransportData.xls"
    }

    try:
        landcover = pd.read_excel(data_files["landcover"])
        population = pd.read_excel(data_files["population"])
        realestate = pd.read_excel(data_files["realestate"])
        transport = pd.read_excel(data_files["transport"])
        # Merge or process as needed
        merged_df = landcover.merge(population, on='city', how='outer') \
                             .merge(realestate, on='city', how='outer') \
                             .merge(transport, on='city', how='outer')
        return merged_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # empty dataframe to prevent crashes

data = load_data()

if data.empty:
    st.stop()  # Stop the app if datasets cannot be loaded


data = load_data()

if data.empty:
    st.stop()  # Stop the app if data isn't loaded

# -----------------------------
# Streamlit App
# -----------------------------
st.title("Urban Data Explorer")
st.subheader("Merged Urban Dataset")
st.dataframe(data)

# -----------------------------
# Filter options
# -----------------------------
st.subheader("Filter Data")
merge_keys = [col for col in data.columns if col.lower() in ['city', 'region', 'area', 'district', 'id']]
selected_key = st.selectbox("Select a column to filter by:", merge_keys)

if selected_key:
    unique_values = data[selected_key].dropna().unique()
    selected_values = st.multiselect(f"Select {selected_key}:", unique_values)
    filtered_data = data[data[selected_key].isin(selected_values)] if selected_values else data
else:
    filtered_data = data

st.write(f"Showing {len(filtered_data)} rows after filtering.")
st.dataframe(filtered_data)

# -----------------------------
# Summary stats
# -----------------------------
st.subheader("Summary Statistics")
st.write(filtered_data.describe(include='number'))  # numeric only to save memory

# -----------------------------
# Download filtered data
# -----------------------------
st.subheader("Download Filtered Data")
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_urban_data.csv",
    mime="text/csv"
)
