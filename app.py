import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Pipeline Anomaly Detection")

# Upload CSV file
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # Show data preview
    st.write("Dataset Preview:")
    st.write(df.head())

    # Select column
    col = st.selectbox("Select column", df.columns)

    # Plot graph
    st.subheader("Line Chart")
    st.line_chart(df[col])

    # Calculate statistics
    mean = df[col].mean()
    std = df[col].std()

    st.write("Mean:", mean)
    st.write("Standard Deviation:", std)

    # Detect anomalies
    anomalies = df[(df[col] > mean + 2*std) | (df[col] < mean - 2*std)]

    # Show anomalies
    st.subheader("Anomalies Detected")
    st.write(anomalies)