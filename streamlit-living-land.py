import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Global Biodiversity Decline')

live=pd.read_excel('living-planet-spread.xlsx')

live=live.drop(axis=1, columns='Unnamed: 0')

live['Year']=live['Year'].astype('object')

live2=pd.pivot_table(live, index='Year', columns='Region', values='Average Index', fill_value=0)

st.subheader('Decline of Average Index by Year')

if st.checkbox('Show Raw Biodiversity Data'):
    st.subheader('Raw Data')
    st.write(live2)
    st.caption("Data Source: World Wildlife Fund (WWF) and Zoological Society of London")

chart=pd.DataFrame(live2, columns=['Africa', 'Asia and Pacific', 'Europe and Central Asia', 'Latin America and the Carribean', 'North America', 'World'])

st.line_chart(chart)

st.caption('Above is a graph plotting the average index of biodiversity per region. Note that all regions are on a steady decline.')


land=pd.read_excel('land_data.xlsx')

st.subheader('Regional Increase in Land Use for Farming by Year')

if st.checkbox('Show Raw Land Area Data'):
    st.subheader('Raw Data')
    st.write(land)
    st.caption('Data Source: UNData')

chart2=pd.DataFrame(land, columns=['Africa', 'Asia', 'Europe', 'South America', 'North America', 'World'])

st.line_chart(chart2)