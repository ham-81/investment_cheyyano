import streamlit as st
import pandas as pd
import numpy as np

st.title('Hey! New investment? :wave:')

DATE_COLUMN = 'date'
DATA_URL = ('file:///Users/hannaabdulmajeed/Downloads/AAPL.csv')
VOLUME_COLUMN = 'volume'

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text('Data Loading....')
data=load_data(10000)
data_load_state.text('Data Loading....done!')

if st.checkbox('Show raw data'):
	st.subheader('Raw Data')
	st.write(data)

st.subheader('Number of stocks by volume')
hist_values = np.histogram(
   data[VOLUME_COLUMN], bins=35, range=(24000000,160000000))[0]
st.bar_chart(hist_values)
