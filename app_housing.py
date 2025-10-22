import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title('California Housing Data (1990) by Xing Pingping')
df = pd.read_csv('housing.csv')

filter = st.slider('Minimal Median House Price:', 0, 500001, 200000) 

st.subheader('see more filters in the sidebar')
st.map(df)

plt.subplots(figsize=(12,6))
sns.histplot(df['median_house_value'].dropna(), bins=30, kde=False, color='tab:blue', edgecolor='w')
plt.title('Histogram of median_house_value')
plt.grid(axis='y', alpha=0.6)
st.pyplot(plt)

loc_col = 'ocean_proximity' if 'ocean_proximity' in df.columns else None
loc_options = sorted(df[loc_col].dropna().unique()) if loc_col else []
loc_selected = st.sidebar.multiselect('Choose the location type', loc_options, default=loc_options)

income_choice = st.sidebar.radio('Choose income level', ('All', 'Low (<=2.5)', 'Medium (>2.5 & <=4.5)', 'High (>4.5)'))

