{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "45d76cb1-6554-40f0-b37f-8de02151f0eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-12 11:18:30.353 No runtime found, using MemoryCacheStorageManager\n",
      "2025-03-12 11:18:30.354 No runtime found, using MemoryCacheStorageManager\n",
      "2025-03-12 11:18:30.355 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:30.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:30.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:30.862 Thread 'Thread-6': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:30.863 Thread 'Thread-6': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "/var/folders/db/k83fvb9n4jvc0k30mrr8127snf90dv/T/ipykernel_8869/2726606283.py:9: DtypeWarning: Columns (5) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  return pd.read_csv(sales_data_path)\n",
      "2025-03-12 11:18:32.713 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.713 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.714 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.714 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.714 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.714 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.844 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.844 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.846 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.846 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.847 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.847 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:32.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "/var/folders/db/k83fvb9n4jvc0k30mrr8127snf90dv/T/ipykernel_8869/2726606283.py:25: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  filtered_df[\"Date\"] = pd.to_datetime(filtered_df[\"Date\"])\n",
      "2025-03-12 11:18:33.085 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.085 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.117 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.119 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.274 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.274 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 11:18:33.275 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
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
   "execution_count": null,
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
