# Data Dictionary

## Overview  
We use two datasets in this project:
1. Air Quality Index (AQI) data (2024)
2. FBI crime data (city-level)

These are merged into a final dataset: merged_aqi_crime.csv.


## Dataset 1: AQI Data (`annual_aqi_by_cbsa_2024.csv`)

| Column | Description |
|--------|------------|
| CBSA | Core-Based Statistical Area (metro area name) |
| CBSA Code | Unique identifier for metro area |
| Year | Year of observation (2024) |
| Days with AQI | Number of days AQI was recorded |
| Good Days | Days with good air quality |
| Moderate Days | Days with moderate air quality |
| Unhealthy for Sensitive Groups Days | Days unhealthy for sensitive populations |
| Unhealthy Days | Days unhealthy for general population |
| Very Unhealthy Days | Days with very poor air quality |
| Hazardous Days | Days with hazardous air conditions |
| Max AQI | Maximum AQI recorded |
| 90th Percentile AQI | AQI value at the 90th percentile |
| Median AQI | Median AQI value |
| Days CO | Days dominated by carbon monoxide |
| Days NO2 | Days dominated by nitrogen dioxide |
| Days Ozone | Days dominated by ozone |
| Days PM2.5 | Days dominated by fine particulate matter |
| Days PM10 | Days dominated by coarse particulate matter |


## Dataset 2: Crime Data (`crime_cleaned.csv`)

| Column | Description |
|--------|------------|
| state | U.S. state |
| city | City name |
| population | Population of the city |
| violent_crime | Total violent crimes |
| murder | Number of murders |
| rape | Number of rapes |
| robbery | Number of robberies |
| aggravated_assault | Number of aggravated assaults |
| property_crime | Total property crimes |
| burglary | Number of burglaries |
| larceny_theft | Number of thefts |
| motor_vehicle_theft | Number of vehicle thefts |
| arson | Number of arson incidents |


## Derived Variables (Created in Analysis)

| Column | Description |
|--------|------------|
| city (cleaned) | Standardized lowercase city name used for merging |
| violent_crime_rate | Violent crimes per 100,000 people |
| property_crime_rate | Property crimes per 100,000 people |
| aqi_quartile | AQI grouped into four categories (best to worst) |


