
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from pandas_profiling import ProfileReport
from pandas.plotting import scatter_matrix
import plotly.graph_objects as go


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


selected_country = st.selectbox('Select a country.', np.sort(df['COUNTRY'].unique()))
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

df_selected_country = df[df["COUNTRY"] == selected_country]
df_selected_country["ORDERDATE"] = pd.to_datetime(df_selected_country["ORDERDATE"])
#-----------------------------------------------------------------------------------------------------------------
st.write('Your selected country is ' + selected_country)
st.table(df_selected_country.describe())




#-----------------------------------------------------------------------------------------------------------------
df2 = df_selected_country.groupby(["ORDERDATE"]).sum()
fig = go.Figure()
fig.add_trace(go.Scatter(x=df2.index, y=df2["SALES"],
                    mode='lines+markers',
                    name='Umsatz'))
fig.update_layout(title="Umsatz-Entwicklung", autosize=False,
width=800, height=800)
st.plotly_chart(fig, use_container_width=True)