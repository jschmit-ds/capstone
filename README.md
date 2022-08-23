# Predicting Road Accident Risk Using Machine Learning
## University of Michigan | Master of Applied Data Science | Capstone Project

<p align="center" width="100%">
    <img width="%05" src="/assets/all_collisions.png"> 
</p>

## Authors
- Eric Moreno
- Joseph Schmit



## TOC
 - [About the Project](#about-the-project)
 - [Repository Organization](#repository-organization)
 - [Getting Started](#getting-started)
 - [Preprocessing Pipeline](#preprocessing-pipeline)
 - [Machine Learning](#machine-learning)

<!-- toc -->

## About the Project
The objective is to combine location and time characteristics to compare the relative likelihood of a collision occurring at a given location and time for Los Angeles County.  In order to accomplish this, we will create a methodology for capturing geolocated information and transforming it into features that can be used to predict collisions.  Various modeling techniques will be implemented and each technique will be scored against each other to determine which model performs best.
The outputs of each model will then be used to describe characteristics of locations that predict collisions to help the end user understand what makes a location more prone to risk.  We also want to provide a dashboard where the user can view a map of LA County where risky areas are highlighted based on the day and time.

<p align="center" width="100%">
    <img width="50%" src="/assets/hexagon_collisions.png"> 
</p>

## Repository Organization
- 00.Concept - Notebooks exploring hexagons and joining data
- 02.Data_Etl - Notebooks for data processing, joining and model data creation
- 03.Model - Notebooks used to create models
- 04.Analysis - Post-modeling analysis

## Getting Started
- Installation
```git clone https://github.com/jschmit-ds/capstone.git```

- [Requirements](/requirements.txt)


## Preprocessing Pipeline
- Download LA county shape file and translate to hexagon grid over the county.
- Download edges and nodes (streets and intersections) from open streets.
    - Clean data
    - Summarize and save as geocoded data
- Download TIMS collision data
    - Clean and attach hexagon ids using latitude and longitude
- Download LA County city shape file
    - Clean and label hexagon ids
- Download amenities (restaurants, schools, bars and colleges). 
    - Clean and summarize by hexagon id.
- Join all location description non-time competent information to hexagons.
- Create collision history features
- Negative sample creation
- NOAA weather data
    - Clean and attach using date and time
- Create Tran/Test/Validation split
- Final data join to create pre-feature engineered model dataset
    - Perform feature engineering
- Creation of dashboard output out of time data.

![alt text](https://github.com/emoreno-hub/capstone/blob/main/assets/Data%20Model.jpg)

## Machine Learning
 - [GLMnet](/03.Model/GLMnet.ipynb)
 - [GBM](/03.Model/GBM.ipynb)
 - [AutoGluon](/03.Model/AutoGluon_Training.ipynb)


## FAQ
