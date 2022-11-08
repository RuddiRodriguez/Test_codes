import streamlit as st
import pandas as pd 

df = pd.read_csv(r'C:\Users\ruddi.garcia\Projects\Requests\20221012_Linda_request\Data\raw_data.csv')

# Create a text element and let the reader know the data is loading.

data_load_state = st.text('Loading data...')

# show the data

st.write(df)