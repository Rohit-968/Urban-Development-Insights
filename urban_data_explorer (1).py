import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    try:
        # Load all 4 datasets directly from Google Sheets
        landcover = pd.read_csv("https://docs.google.com/spreadsheets/d/1hLnm7JKVpEwVjTtelJPH0Wv2mBQiczEX/export?format=csv")
        population = pd.read_csv("https://docs.google.com/spreadsheets/d/1aNeMKxCFqYdJJhgCacIMaVq3gCl88jyI/export?format=csv")
        realestate = pd.read_csv("https://docs.google.com/spreadsheets/d/1GhSqb-RiPC3cn_5rWdhXWUTFYMqhcRxC/export?format=csv")
        transport = pd.read_csv("https://docs.google.com/spreadsheets/d/1q9EXdpJMW9fDbVDdS9RIMRAZpzP9qrBs/export?format=csv")

        # Merge everything on the "city" column (edit if your join key is different)
        merged_df = (
            landcover
            .merge(population, on="city", how="outer")
            .merge(realestate, on="city", how="outer")
            .merge(transport, on="city", how="outer")
        )

        return merged_df

    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

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
