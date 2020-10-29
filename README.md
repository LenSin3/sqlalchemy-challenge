# **sqlalchemy-challenge**

## **Objectives**

This project involves analysing data from 9 weather staions in Hawaii between **1/1/2010** and **8/23/2017**. The data is stored in a sqlite database **hawaii.sqlite** consisting of two tables:

- **measurements**

This table contains precipitation and temperature points observed, together with station id and dates measurements were taken. It has a total of 19550 points spanning the entire period mentioned above.

- **station**

This table contains the id, name, geographic location(longitude and latitude) and elevation of each of the 9 stations in the study</br>.

### **Tasks**

The main tasks to be accomplished are seen below:

#### **Precipitation Analysis**

- Explore the data and perform climate analysis.

- Design queries to retrieve the last 12 months of precipitation data.

- Plot precipitation values for the 12 months period.

#### **Station Analysis**

- Design a query to calculate the total number of stations.

- Design queries to find the most active station
  
  - List the stations and observation counts in descending order.

  - Station with the highest number of observations.

- Design a query to retrieve the last 12 months of temperature observation data.

   - Plot the results as a histogram.

#### **Climate App**

- Design a Flask API based on the above queries(Precipitation and Station).

- In Flask, create the following routes:
 
  - Home page route ('**/**') listing all the routes in the app.

  - Precipitation route ('**/api/v1.0/precipitation**') that returns a JSON representation of a dictionary containing date and precipitation.

  - Station route ('**/api/v1.0/stations**') returning a JSON list of stsions in the dataset.

  - Observed temperature ('**/api/v1.0/tobs**') route returns a JSON list of temperature observations (TOBS) for the previous year.

  - Dynamic route ('**/api/v1.0/<start>**')  to return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date.

  - Dynamic route ('**/api/v1.0/<start>/<end>**')  to return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start and end date.


### **Bonus Tasks**

The following tasks were also completed as bonus:

#### **Temperature Analysis I**

- Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

- Use the t-test to determine whether the difference in the means, if any, is statistically significant.


#### **Temperature Analysis II**

- Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year.

- Plot the min, avg, and max temperature from previous query as a bar chart.


#### **Daily Rainfall Average**

- Calculate the rainfall per weather station using the previous year's matching dates.

- Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures. Use the `daily_normals` function that will calculate the daily normals for a specific date.

- Use Pandas to plot an area plot (`stacked=False`) for the daily normals.


## **Dependencies**

### **Jupyter Notebook**

- SQLALchemy ORM

- Pandas

- Matplotlib

- Datetime

- Scipy


### **Python script**

- Flask

- SQLALchemy ORM

- Datetime


## **Environment**

- SQLite database

- Python 3.6


## **Files**

- **climate_starter.ipynb** containing Precipitation and Station analysis

- **app.y** is the climate app created using Flask API and queries from previous analysis.

- **daily_del_precipitation.png** plot of precipitation data.

- **tobs_hist.png** histogram of observed temperatures.

- **trip_bar_chart.png** bar chart with error bar of average temperature.

- **daily_rainfall.png** area plot of precipitation data.

- **Resources** folder containing **hawaii.sqlite** database.