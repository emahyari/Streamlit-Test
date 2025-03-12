{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "45d76cb1-6554-40f0-b37f-8de02151f0eb",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'plotly'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[9], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mplotly\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexpress\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpx\u001b[39;00m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;66;03m# Load the sales data\u001b[39;00m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;129m@st\u001b[39m\u001b[38;5;241m.\u001b[39mcache_data\n\u001b[1;32m      7\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mload_data\u001b[39m():\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'plotly'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Load the sales data\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    sales_data_path = \"sales_data.csv\"  # Ensure the correct file path\n",
    "    return pd.read_csv(sales_data_path)\n",
    "\n",
    "sales_df = load_data()\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"📊 Sales Dashboard\")\n",
    "\n",
    "# Sidebar filters\n",
    "st.sidebar.header(\"Filter Options\")\n",
    "selected_country = st.sidebar.selectbox(\"Select Country\", sales_df[\"Country\"].unique())\n",
    "selected_year = st.sidebar.selectbox(\"Select Year\", sorted(sales_df[\"Year\"].unique()))\n",
    "\n",
    "# Filter data based on selection\n",
    "filtered_df = sales_df[(sales_df[\"Country\"] == selected_country) & (sales_df[\"Year\"] == selected_year)]\n",
    "\n",
    "# Aggregate sales by date\n",
    "filtered_df[\"Date\"] = pd.to_datetime(filtered_df[\"Date\"])\n",
    "aggregated_sales = filtered_df.groupby(\"Date\")[\"Revenue\"].sum().reset_index()\n",
    "\n",
    "# Display filtered data\n",
    "st.subheader(f\"Sales Data for {selected_country} in {selected_year}\")\n",
    "st.write(filtered_df)\n",
    "\n",
    "# Line chart visualization\n",
    "fig = px.line(aggregated_sales, x=\"Date\", y=\"Revenue\", title=\"Sales Trend\")\n",
    "st.plotly_chart(fig)\n",
    "\n",
    "st.sidebar.markdown(\"---\")\n",
    "st.sidebar.caption(\"📌 Built with Streamlit and Plotly\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "58c9de37-56db-49c0-b908-2c5e9d8b9afb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
