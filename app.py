import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ✅ Set page config FIRST
st.set_page_config(
    page_title="RFM Customer Segmentation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Description
st.title("📊 RFM Customer Segmentation Dashboard")
st.markdown("""
Welcome to the interactive RFM segmentation dashboard. 
This app allows you to:
- Upload your RFM-segmented customer data (CSV)
- Explore clusters using plots and filters
- Understand customer behavior based on Recency, Frequency, and Monetary values.
""")

# Sidebar - Upload file
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data loaded successfully!")

    # Sidebar filters
    st.sidebar.header("Filter Options")
    cluster_filter = st.sidebar.multiselect(
        "Select Clusters", options=sorted(df['Cluster'].unique()), default=df['Cluster'].unique()
    )

    filtered_df = df[df['Cluster'].isin(cluster_filter)]

    # Tabs for views
    tab1, tab2, tab3 = st.tabs(["📈 Cluster Overview", "📊 Distribution", "🧮 Data Table"])

    with tab1:
        st.subheader("3D RFM Cluster View")
        fig = px.scatter_3d(
            filtered_df,
            x='Recency',
            y='Frequency',
            z='Monetary',
            color='Cluster',
            opacity=0.7,
            title="3D Scatter of Clusters"
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Boxplots by Cluster")
        metric = st.selectbox("Select Metric", ['Recency', 'Frequency', 'Monetary'])
        fig2 = px.box(filtered_df, x='Cluster', y=metric, color='Cluster', title=f"{metric} Distribution by Cluster")
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.subheader("Segmented Customer Data")
        st.dataframe(filtered_df, use_container_width=True)

else:
    st.warning("👈 Please upload an RFM CSV file to begin.")
