import streamlit as st
import pandas as pd
# import plotly.express as px
import matplotlib.pyplot as plt

# Load the sales data
@st.cache_data
def load_data():
    sales_data_path = "sales_data.csv"  # Ensure the correct file path
    return pd.read_csv(sales_data_path)

sales_df = load_data()

# Streamlit UI
st.title("📊 Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", sales_df["Country"].unique())
selected_year = st.sidebar.selectbox("Select Year", sorted(sales_df["Year"].unique()))

# Filter data based on selection
filtered_df = sales_df[(sales_df["Country"] == selected_country) & (sales_df["Year"] == selected_year)]

# Aggregate sales by date
filtered_df["Date"] = pd.to_datetime(filtered_df["Date"])
aggregated_sales = filtered_df.groupby("Date")["Revenue"].sum().reset_index()

# Display filtered data
st.subheader(f"Sales Data for {selected_country} in {selected_year}")
st.write(filtered_df)

# Line chart visualization
# fig = px.line(aggregated_sales, x="Date", y="Revenue", title="Sales Trend")
aggregated_sales.plot(figsize = (15, 5))
st.plotly_chart(fig)

st.sidebar.markdown("---")
st.sidebar.caption("📌 Built with Streamlit and Plotly")