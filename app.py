
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

# ==== Visualization 1: Estimated vs Actual ====
st.markdown("### Estimated vs Actual Earnings (Hypothesis 1)")
fig1, ax1 = plt.subplots()
sns.regplot(x='VALUE', y='ACTUAL', data=filtered_df, ax=ax1, scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'})
ax1.set_title(f"{selected_ticker}: Estimate vs Actual")
ax1.set_xlabel("Estimated Earnings (VALUE)")
ax1.set_ylabel("Actual Earnings (ACTUAL)")
st.pyplot(fig1)

# ==== Visualization 2: Forecast Error Trend ====
st.markdown("### Forecast Error Over Time (Hypothesis 3)")
avg_error_by_year = df.groupby('YEAR')['ERROR'].mean().reset_index()
fig2, ax2 = plt.subplots()
ax2.plot(avg_error_by_year['YEAR'], avg_error_by_year['ERROR'], marker='o')
ax2.set_title("Average Forecast Error by Year")
ax2.set_xlabel("Year")
ax2.set_ylabel("Average Absolute Error")
ax2.grid(True)
st.pyplot(fig2)

# ==== Insights Section ====
st.markdown("### Insights")
st.write("""
- Analyst estimates show a strong positive correlation with actual earnings (correlation ≈ 0.95).
- Forecast accuracy has improved over time, with average error decreasing since the early 2000s.
""")

# ==== Recommendations Section ====
st.markdown("### Recommendations")
st.write("""
- Financial analysts and decision-makers can rely more confidently on recent forecasts due to improved accuracy.
- Continued tracking of forecast accuracy is recommended to support long-term financial planning.
""")
