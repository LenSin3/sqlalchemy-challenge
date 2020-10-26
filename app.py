import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    # Calculate the date 1 year ago from the last data point in the database
    date_delta = dt.date(2017, 8, 23) - dt.timedelta(days = 365.25)
    print("date_delta :", date_delta)

    # Perform a query to retrieve the data and precipitation scores
    data_precip = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= date_delta).all()

    session.close()

    all_precipitation = []
    for date, prcp in data_precip:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query list of distinct stations in the dataset
    stations_dstnct = session.query(distinct(Measurement.station)).all()

    session.close()

    return jsonify(stations_dstnct)

@app.route("/api/v1.0/tobs")
def temp_obs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the dates and temperature observations of the most active station for the last year of data
    # List the stations and the counts in descending order.

    # Time delta of 1 year for latest date for which observation was made
    most_active_date_delta = dt.date(2017, 8, 18) - dt.timedelta(days = 365.25)

    # Dates and temperatures of 1 year time delta at station with highest number of temperature observations
    most_active_date_delta_tobs = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= most_active_date_delta).all()

    session.close()


    temp_obs = []
    for date, tobs in most_active_date_delta_tobs:
        temp_obs_dict = {}
        temp_obs_dict['date'] = date
        temp_obs_dict['tobs'] = tobs
        temp_obs.append(temp_obs_dict)

    return jsonify(temp_obs)

if __name__ == '__main__':
    app.run(debug=True)


