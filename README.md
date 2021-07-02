# Costa Rica earthquake activity dashboard using Streamlit and Plotly

This application was developed using pure python. Currently the application is deployed on heroku:https://crearthquakes.herokuapp.com/

I used the library Streamlit for building the UI and the Web interface. 

https://streamlit.io/

For the Map and data visualizations I used the python library plotly.
https://plotly.com/python/

The earthquake data is scrape from the OVSICORI website where they keep track of every recent earthquake register in Costa Rica. 

http://www.ovsicori.una.ac.cr/

The main idea of this project was to improve the user experience when exploring the data for the most recent earthquakes in Costa Rica.. 

The Web application is divided into 4 sections:

  1. A table presenting the data from the website: http://www.ovsicori.una.ac.cr/index.php/tabla-sismos-recientes.

  ![alt text](https://raw.githubusercontent.com/georgedevcode/cr_earthquake_dashboard/master/img/earthquake_data.png)

  2. An interactive map showcasing the location where the earthquake was registered and the magnitude density.

  ![alt text](https://raw.githubusercontent.com/georgedevcode/cr_earthquake_dashboard/master/img/map.png)

    ### Side note: The original map from the oficial OVSICORI website only allows the user to see a single point referring to an earthquake.

  ![alt text](https://raw.githubusercontent.com/georgedevcode/cr_earthquake_dashboard/master/img/old_map.png)

  3. A magnitude chart to keep track of the magnitude level for the earthquakes.

   ![alt text](https://raw.githubusercontent.com/georgedevcode/cr_earthquake_dashboard/master/img/line_chart.png)

  5. A bubble chart for easily identify which earthquake had the highes magnitude record.
    ![alt text](https://raw.githubusercontent.com/georgedevcode/cr_earthquake_dashboard/master/img/buble_chart.png)
   
 Created by: https://www.linkedin.com/in/ing-jorgecerdas/
