import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st



st.title('Global Biodiversity Decline')

st.write(' ')
st.write(' ')
st.write(' ')

live=pd.read_excel('living-planet-spread.xlsx', dtype={'Year' : str})

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

st.caption('Above is a graph plotting the average index (y-axis) of biodiversity per region. Note that all regions are on a steady decline, particularly Latin America which has a sharper decline than all other regions. One possible cause of this could be deforestation related to farming. See the below graph.')

st.write(' ')
st.write(' ')
st.write(' ')




land=pd.read_excel('fao_land_data_spread.xlsx', dtype={'Year':str})
land=land.set_index('Year')

st.subheader('Regional Increase in Land Use for Farming by Year')

if st.checkbox('Show Raw Land Area Data'):
    st.subheader('Raw Data')
    st.write(land)
    st.caption('Data Source: UNData')

chart2=pd.DataFrame(land, columns=['Africa', 'Asia', 'Europe', 'South America', 'North America'])
chart3=pd.DataFrame(land, columns=['World'])

st.line_chart(chart2)

st.caption('Above is a graph plotting the area of farmland used per region. The area (y-axis) is shown in Hectare (Ha), with 1Ha equating to 2.47 acres. As you can see, the graphs line up well, with Europe seeing an increase in biodiversity in the 1990s as their land devoted to farming decreased. Latin America does not see a very dramatic increase, though the introduction of invasive species of plants and animals can also be attributed to their decline.')

st.write(' ')
st.write(' ')
st.write(' ')

st.subheader('Global Increase in Land Use for Farming by Year')

st.line_chart(chart3)

st.caption('I put the Global area of farmland in its own graph as the area was so extreme that it flattened the line graph of the individual regions. Note the heavy drop around the 1990s, around the same time that four of the five regions had an increase in farmland usage.')