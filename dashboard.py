{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "45d76cb1-6554-40f0-b37f-8de02151f0eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-12 10:39:15.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.489 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.491 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.491 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.492 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.495 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.495 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.497 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.497 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-12 10:39:15.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "st.title(\"📊 Streamlit Dynamic Dashboard\")\n",
    "\n",
    "# Sidebar controls\n",
    "st.sidebar.header(\"User Controls\")\n",
    "num_points = st.sidebar.slider(\"Select number of data points\", min_value=10, max_value=100, value=50)\n",
    "\n",
    "# Function to generate data dynamically\n",
    "def generate_data(n):\n",
    "    time_series = pd.date_range(start=\"2023-01-01\", periods=n, freq=\"D\")\n",
    "    values = np.random.randn(n).cumsum()\n",
    "    return pd.DataFrame({\"Date\": time_series, \"Value\": values})\n",
    "\n",
    "# Initialize or update session state\n",
    "if \"data\" not in st.session_state:\n",
    "    st.session_state.data = generate_data(num_points)\n",
    "\n",
    "if st.button(\"🔄 Refresh Data\"):\n",
    "    st.session_state.data = generate_data(num_points)\n",
    "\n",
    "# Display data table\n",
    "st.subheader(\"Generated Data\")\n",
    "st.write(st.session_state.data)\n",
    "\n",
    "# Plot chart\n",
    "st.subheader(\"Data Visualization\")\n",
    "st.line_chart(st.session_state.data.set_index(\"Date\"))\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a6b801b8-4702-40c2-a604-95ead645591f",
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
