import seaborn as sns
import streamlit as st

st.title("Jessica's Iris Analysis App 🐝")

iris_df = sns.load_dataset("iris")

st.header("Dataset")
st.dataframe(data=iris_df)

st.header("Dataset Description")
st.dataframe(data=iris_df.describe())

x = st.selectbox(label="Enter x-axis column: ", options=iris_df.columns)
y = st.selectbox(label="Enter y-axis column: ", options=iris_df.columns)

st.scatter_chart(data=iris_df, x=x, y=y, color="species")