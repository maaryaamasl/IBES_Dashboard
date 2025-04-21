
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("IBES_cleaned.csv")

# Ensure necessary columns exist
df['YEAR'] = df['ACTDATS'].astype(str).str[:4].astype(int)
df['ERROR'] = (df['VALUE'] - df['ACTUAL']).abs()

# Page title
st.title("Earnings Forecast Analysis Dashboard")

# ==== Introduction ====
st.markdown("### Introduction")
st.write("""
This dashboard explores how analyst earnings forecasts compare to actual reported earnings over time. 
It includes correlation analysis and error trends to test two data-driven hypotheses.
""")

# ==== Dropdown for company ticker ====
selected_ticker = st.selectbox("Select a company ticker", df['TICKER'].unique())
filtered_df = df[df['TICKER'] == selected_ticker]

# ==== Univariate Analysis: Box Plot of Actual Earnings ====
st.markdown("### Univariate Analysis: Actual Earnings by Ticker")
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.boxplot(x='TICKER', y='ACTUAL', data=df, ax=ax4)
ax4.set_title("Distribution of Actual Earnings by Company")
ax4.set_xlabel("Company Ticker")
ax4.set_ylabel("Actual Reported Earnings")
ax4.tick_params(axis='x', rotation=90)
st.pyplot(fig4)

# ==== Visualization 1: Estimated vs Actual ====
st.markdown("### Estimated vs Actual Earnings")
fig1, ax1 = plt.subplots()
sns.regplot(x='VALUE', y='ACTUAL
