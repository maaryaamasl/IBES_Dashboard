import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Load Data ===
st.title("📊 IBES Interactive Dashboard")
data = pd.read_csv("IBES.csv")

# === Identify numeric columns ===
numeric_cols = data.select_dtypes(include='number').columns.tolist()

# === Sidebar: Controls ===
st.sidebar.header("🔧 Controls")

# 1. Dropdown to select numeric variable for hist/box
selected_var = st.sidebar.selectbox("Select a numeric variable", numeric_cols)

# 2. Slider for histogram bin count
bin_count = st.sidebar.slider("Number of bins (for histogram)", 5, 50, 20)

# 3. Checkbox to toggle correlation heatmap
show_corr = st.sidebar.checkbox("Show Correlation Heatmap", value=True)

# 4. Multiselect for pairplot variables
pairplot_vars = st.sidebar.multiselect("Select variables for pairplot", numeric_cols, default=numeric_cols[:3])

# === Visualization 1: Histogram ===
st.subheader(f"📈 Histogram of {selected_var}")
fig1, ax1 = plt.subplots()
sns.histplot(data[selected_var].dropna(), bins=bin_count, kde=True, ax=ax1)
st.pyplot(fig1)

# === Visualization 2: Boxplot ===
st.subheader(f"📦 Boxplot of {selected_var}")
fig2, ax2 = plt.subplots()
sns.boxplot(y=data[selected_var].dropna(), ax=ax2)
st.pyplot(fig2)

# === Visualization 3: Correlation Heatmap ===
if show_corr:
    st.subheader("🧊 Correlation Heatmap of Numerical Columns")
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    corr_matrix = data[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

# === Visualization 4: Pairplot of Selected Variables ===
if len(pairplot_vars) >= 2:
    st.subheader("🔁 Pairwise Scatter Plot")
    fig4 = sns.pairplot(data[pairplot_vars], corner=True)
    st.pyplot(fig4)
else:
    st.warning("Please select at least two variables for the pairplot.")
