import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit import config

csv_path = "https://raw.githubusercontent.com/georgedevcode/cr_earthquakes_dashboard/master/Data/cr_earthquakes.csv"

def printDensityMap(data_selected_province):
    fig = px.density_mapbox(data_selected_province, lat="Latitude", lon="Longitude", z="Magnitude", radius=10, mapbox_style="open-street-map", zoom=5)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

def printMgLineChart(data_selected_province):
    data = data_selected_province["Magnitude"]
    return data

def printBubbleScatter(data_selected_province):
    fig = px.scatter(data_selected_province, x="Date", y="Magnitude",hover_name="Province",hover_data=["Location"], size="Magnitude", color="Magnitude")
    return fig

@st.cache
def getData():
    #Temporary function to read the data from a CSV file.
    #In the future we are actually going to get the data from a azure blob storage
    df = pd.read_csv(csv_path)
    df = df.drop(columns=["Revisado","Autor","Mapa"])
    df = df.dropna()
    df = df.rename(columns={"Fecha":"Date","Hora":"Local Time","Magnitud":"Magnitude","Profundidad":"Deepth(KM)", "Latitud":"Latitude", "Longitud":"Longitude", "Localizacion":"Location","Provincia":"Province"})
    df["Date"] = (pd.to_datetime(df["Date"], infer_datetime_format=True)).dt.date
    df = df.sort_values(by=["Date"], ascending=False)
    df = df.reset_index(drop=True)
    return df

def main():
    #Some title and descriptive text
    st.title("Earthquake activity")

    #Getting the data and displaying the dataframe in the dashboard
    data = getData()
    
    #Multiple selection for the provinces
    provinces_options = list(data.Province.unique())
    st.sidebar.header("Costa Rica Earthquakes")
    st.sidebar.caption("This dashboard contains information for every recent earhtquake registered in Costa Rica.The data is collected from the OVSICORI website: http://www.ovsicori.una.ac.cr/index.php/sismologia/sistemas-de-consulta")
    province = st.sidebar.multiselect("Please select a province:",options=provinces_options, default=provinces_options)
    data_selected_province = data[data.Province.isin(province)]
    st.sidebar.caption("This dashboard was done by Jorge Cerdas https://www.linkedin.com/in/ing-jorgecerdas/")

    #Print the dataframe based on the user selection, 
    #By default all the locations are deisplayed
    st.dataframe(data_selected_province, width=4000, height=510)

    #Printing the density map
    st.title("Earthquakes density map")
    hMap = printDensityMap(data_selected_province)
    st.plotly_chart(hMap,use_container_width=True)
    
       
    #Printing magnitude line chart
    st.title("Magnitude line chart")
    magChart = printMgLineChart(data_selected_province)
    st.line_chart(magChart)

    st.title("Earthquakes bubble chart")
    scatter_fig = printBubbleScatter(data_selected_province)
    st.plotly_chart(scatter_fig, use_container_width=True)

if __name__ == "__main__":

    #Here we are setting the page configuration setting
    st.set_page_config(
        page_title="Costa Rica Earthquake Activity",
        page_icon="🇨🇷",
        layout="wide",
        initial_sidebar_state="auto"
    )

    main()
