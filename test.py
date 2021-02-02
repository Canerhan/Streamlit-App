
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


st.set_page_config(
page_title="Ja Hallo",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded")
st.title('Analyse')



@st.cache
def get_data():
    url = r'https://raw.githubusercontent.com/Canerhan/data-analytics-with-Pandas-Hvplot/main/Sales.csv'
    df = pd.read_csv(url,encoding='latin1', sep=',', error_bad_lines=False)
    return df

df = get_data()


if st.selectbox('Select a country.', np.sort(df['COUNTRY'].unique())):
    st.write("Here's our first attempt at using data to create a table:")
    st.write(df)

st.write(df.describe())