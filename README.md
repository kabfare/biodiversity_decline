# Global Biodiversity Decline as Related to Farming

A data analytics project attempting to correlate the global decline of biodiversity--the variety of plants, animals, insects, and fish--with the increase in farmland per region. The project contains two .csv files, two Jupyter notebooks, and two .xlsx files. My Streamlit code is also stored in an .py file. Each .ipynb takes it's assigned .csv files, cleans and wrangles the data, graphs it, and exports the cleaned data to an Excel file to be used in the Streamlit code. Deforestation and land destruction related to farming is only one of the many causes of the biodiversity decline across the globe. The streamlit app takes each graph and correlates the graph showing the decline in biodiversity with the graph showing the increase in land dedicated to farming.


### Instructions:
1. Refer to **requirements.txt**.
2. Ensure modules are installed and Python is updated to at least 3.9.16.
3. Open and run **living_planet.ipynb.** This will display a graph and create an Excel file named 'living-planet-spread.xlsx'.
4. Open and run **fao_land_data.ipynb**. This will display a graph and create an Excel file named 'fao_land_data_spread.xlsx'.
5. Open **streamlit-living-land.py**.
6. In terminal, run `streamlit run streamlit-living-land.py`. This will open a new window in your browser of the streamlit app.
7. Alternatively, you can visit this [link](https://kabfare-biodiversity-decline-streamlit-living-land-xrt9r7.streamlit.app) to view the app.


### Features:
1. Read in data from a local csv and excel file.
2. Use built-in pandas functions to clean and manipulate data.
3. Write custom functions to operate on data.
4a. Make two basic plots with matplotlib.
4b. Use GUI library like streamlit to make an interactive visualization.
5. Write markdown cells in Jupyter explaining the code.
