import streamlit as st
import pandas as pd

data = {
            'Course Name': ['MySql', 'Linux', 'Hadoop', 'Python', 'DevOps', 'Azure', 'Pyspark'], 
            'Duration': ['30 days', '15 days', '20 days', '35 days', '35 days', '25 days', '20 days'],
            'Fees': ['8000', '5000', '10000', '10000', '20000', '10000', '7000']
    }
df = pd.DataFrame(data)

st.dataframe(df)

