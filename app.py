import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("IBES_cleaned.csv")

# Prepare columns
df['YEAR'] = df['ACTDATS'].astype(str).str[:4].astype(int)
df['ERROR'] = (df['VALUE'] - df['ACTUAL']).abs()

# Page title
st.title("Earnings Forecast Analysis Dashboard")

# ==== Introduction ====
st.markdown("### Introduction")
st.write("""
This dashboard explores how analyst earnings forecasts compare to actual reported earnings over time. 
It includes correlation analysis, error trends, and univariate analysis to evaluate forecast reliability.
""")

# ==== Dropdown for ticker selection ====
selected_ticker = st.selectbox("Select a company ticker", df['TICKER'].unique())
filtered_df = df[df['TICKER'] == selected_ticker]

# ==== Univariate Analysis ====
st.markdown("### Actual Earnings")
fig_uni, ax_uni = plt.subplots(figsize=(10, 5))
sns.boxplot(x='TICKER', y='ACTUAL', data=df, ax=ax_uni)
ax_uni.set_title("Distribution of Actual Earnings by Company")
ax_uni.set_xlabel("Company Ticker")
ax_uni.set_ylabel("Actual Reported Earnings")
ax_uni.tick_params(axis='x', rotation=90)
st.pyplot(fig_uni)

# ==== Visualization 1: Estimated vs Actual (Hypothesis 1) ====
st.markdown("### Estimated vs Actual Earnings")
fig1, ax1 = plt.subplots()
sns.regplot(x='VALUE', y='ACTUAL', data=filtered_df, ax=ax1, scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'})
ax1.set_title(f"{selected_ticker}: Estimate vs Actual")
ax1.set_xlabel("Estimated Earnings (VALUE)")
ax1.set_ylabel("Actual Earnings (ACTUAL)")
st.pyplot(fig1)

# ==== Visualization 2: Forecast Error Over Time (Hypothesis 3) ====
st.markdown("### Forecast Error Over Time")
avg_error_by_year = df.groupby('YEAR')['ERROR'].mean().reset_index()
fig2, ax2 = plt.subplots()
ax2.plot(avg_error_by_year['YEAR'], avg_error_by_year['ERROR'], marker='o')
ax2.set_title("Average Forecast Error by Year")
ax2.set_xlabel("Year")
ax2.set_ylabel("Average Absolute Error")
ax2.grid(True)
st.pyplot(fig2)

# ==== Insights ====
st.markdown("### Insights")
st.write("""
- Analyst estimates show a strong positive correlation with actual earnings (correlation ≈ 0.95).
- Forecast accuracy has improved over time, with average error decreasing since the early 2000s.
- Some tickers have greater variance in actual reported earnings, as shown in the box plot.
""")

# ==== Recommendations ====
st.markdown("### Recommendations")
st.write("""
- Organizations can place more trust in analyst earnings forecasts, especially in recent years.
- Further analysis could focus on sectors or events that may affect estimate accuracy.
""")
