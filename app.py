import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("IBES_cleaned.csv")
df['YEAR'] = df['ACTDATS'].astype(str).str[:4].astype(int)
df['ERROR'] = (df['VALUE'] - df['ACTUAL']).abs()

st.title("Earnings Forecast Analysis Dashboard")

st.markdown("### Introduction")
st.write("This dashboard explores analyst earnings estimates and actual earnings over time.")

selected_ticker = st.selectbox("Select a company ticker", df['TICKER'].unique())
filtered_df = df[df['TICKER'] == selected_ticker]

# Univariate
st.markdown("### Univariate Analysis: Actual Earnings by Ticker")
fig_uni, ax_uni = plt.subplots(figsize=(10, 5))
sns.boxplot(x='TICKER', y='ACTUAL', data=df, ax=ax_uni)
ax_uni.tick_params(axis='x', rotation=90)
st.pyplot(fig_uni)

# Visualization 1
st.markdown("### Estimated vs Actual Earnings")
fig1, ax1 = plt.subplots()
sns.regplot(x='VALUE', y='ACTUAL', data=filtered_df, ax=ax1, scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'})
st.pyplot(fig1)

# Visualization 2
st.markdown("### Forecast Error Over Time")
avg_error_by_year = df.groupby('YEAR')['ERROR'].mean().reset_index()
fig2, ax2 = plt.subplots()
ax2.plot(avg_error_by_year['YEAR'], avg_error_by_year['ERROR'], marker='o')
st.pyplot(fig2)

st.markdown("### Insights")
st.write("- Strong correlation between estimated and actual earnings.")
st.write("- Forecast error has decreased over time.")

st.markdown("### Recommendations")
st.write("- Rely on recent analyst forecasts with more confidence.")
