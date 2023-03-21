import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt



st.title('Global Biodiversity Decline')

st.write(' ')
st.write(' ')
st.write(' ')

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

fig, ax=plt.subplots(figsize=(12,6))
ax.plot(chart)
ax.set(xlabel='Year', ylabel='Index (%)')
ax.legend(['Africa', 'Asia', 'Europe', 'South America', 'North America'])
st.pyplot(fig)

st.caption('Above is a graph plotting the average index of biodiversity per region. Note that all regions are on a steady decline, particularly Latin America which has a sharper decline than all other regions. One possible cause of this could be deforestation related to farming. See the below graph.')

st.write(' ')
st.write(' ')
st.write(' ')




land=pd.read_excel('fao_land_data_spread.xlsx')
land=land.set_index('Year')

st.subheader('Regional Increase in Land Use for Farming by Year')

if st.checkbox('Show Raw Land Area Data'):
    st.subheader('Raw Data')
    st.write(land)
    st.caption('Data Source: UNData')

chart2=pd.DataFrame(land, columns=['Africa', 'Asia', 'Europe', 'South America', 'North America'])
chart3=pd.DataFrame(land, columns=['World'])

fig, ax=plt.subplots(figsize=(12,6))
ax.plot(chart2)
ax.set(xlabel='Year', ylabel='Area (1000 Ha)e+06')
ax.legend(['Africa', 'Asia', 'Europe', 'South America', 'North America'])
st.pyplot(fig)

st.caption('Above is a graph plotting the area of farmland used per region. The area is shown as 1000 Ha, with one thousand Ha equating to 2,471.05 acres. As you can see, the graphs line up well, with Europe seeing an increase in biodiversity in the 1990s as their lad devoted to farming decreased. Latin America does not see a very dramatic increase, though the introduction of invasive species of plants and animals can also be attributed to their decline.')

st.write(' ')
st.write(' ')
st.write(' ')

st.subheader('Global Increase in Land Use for Farming by Year')

fig, ax=plt.subplots(figsize=(12,6))
ax.plot(chart3)
ax.set(xlabel='Year', ylabel='Area (1000 Ha)e+06')
st.pyplot(fig)

st.caption('I put the Global area of farmland in its own graph as the area was so extreme that it flattened the line graph of the individual regions. Note the heavy drop around the 1990s, around the same time that three regions had an increase in farmland.')