import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Set page config FIRST
st.set_page_config(
    page_title="Enhanced RFM Customer Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar - File Upload
# -----------------------------
st.sidebar.header("Upload RFM CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# -----------------------------
# Function: Segment Assignment
# -----------------------------
def assign_segment(score):
    if score >= 9:
        return "Best Customers"
    elif score >= 6:
        return "Loyal Customers"
    elif score >= 4:
        return "At Risk"
    else:
        return "Churned"

# -----------------------------
# Main Interface
# -----------------------------
st.title("📊 Enhanced RFM Customer Segmentation Dashboard")
st.markdown("""
This dashboard analyzes customer behavior using **Recency**, **Frequency**, and **Monetary** values.

Use the sidebar to upload a dataset and interact with segmentation insights.
""")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    with st.sidebar.expander("🔍 Filter Data"):
        r_range = st.slider("Recency Range", int(df['Recency'].min()), int(df['Recency'].max()), (20, 80))
        f_range = st.slider("Frequency Range", int(df['Frequency'].min()), int(df['Frequency'].max()), (1, 3))
        m_range = st.slider("Monetary Range", int(df['Monetary'].min()), int(df['Monetary'].max()), (0, 10000))

    filtered_df = df[
        (df['Recency'].between(*r_range)) &
        (df['Frequency'].between(*f_range)) &
        (df['Monetary'].between(*m_range))
    ]

    # Score and segment if not already done
    if 'RFM_Score' not in df.columns:
        df['RFM_Score'] = df[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)
    df['Segment'] = df['RFM_Score'].apply(assign_segment)

    st.subheader("📈 Segment Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", len(df))
    col2.metric("Best Customers", sum(df['Segment'] == "Best Customers"))
    col3.metric("Loyal Customers", sum(df['Segment'] == "Loyal Customers"))
    col4.metric("At Risk", sum(df['Segment'] == "At Risk"))

    # Pie chart
    fig1 = px.pie(df, names='Segment', title='Customer Segment Distribution')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📌 Average RFM by Segment")
    avg_rfm = df.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean().round(2)
    st.dataframe(avg_rfm)

    st.subheader("📊 RFM Distributions")
    fig2 = px.histogram(filtered_df, x='Recency', nbins=30, title='Recency Distribution')
    fig3 = px.histogram(filtered_df, x='Frequency', nbins=30, title='Frequency Distribution')
    fig4 = px.histogram(filtered_df, x='Monetary', nbins=30, title='Monetary Distribution')
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("📤 Download Segmented Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "RFM_segmented.csv", "text/csv")

else:
    st.warning("Please upload an RFM-segmented CSV file to begin.")
