import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1 — App Title & Data Setup

st.title("Sales Dashboard")
st.subheader("Analyze product sales by category")

# Create a hardcoded DataFrame
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Office"],
    "Sales": [1500, 300, 450, 800, 600]
}

df = pd.DataFrame(data)

# Task 2 — Sidebar Filter

st.sidebar.header("Filter Options")

# Unique categories
categories = df["Category"].unique()

# Selectbox in sidebar
selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Data Filtering

filtered_df = df[df["Category"] == selected_category]

# Display Output

st.write(f"### Showing data for: {selected_category}")

# Display table
st.dataframe(filtered_df)

# Line chart for Sales
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])