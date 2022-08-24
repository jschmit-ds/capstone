<p align="left" width="100%">
<img width="400" src="https://github.com/emoreno-hub/capstone/blob/main/assets/logo-header.png"> 
    </p>
    
# Predicting Road Accident Risk Using Machine Learning
## Master of Applied Data Science Capstone

<p align="center" width="100%">
    <img width="450" src="/assets/all_collisions.png "> 
</p>

## Authors
- Eric Moreno
- Joseph Schmit

## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"></a> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <img src="https://altair-viz.github.io/_static/altair-logo-light.png" alt="Altair" width="40" height="40"/> <img src="https://matplotlib.org/3.1.0/_static/logo2.png" alt="Matplotlib"  height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" height="40"/> </a> <img src="https://i.pcmag.com/imagery/reviews/058odIpsFui7XT7sYt0XBFr-9..v1569472704.jpg" alt="S3" height="40"/> </a> <img src="https://miro.medium.com/max/300/1*jbYRQa6__lU3EAzdkA_fJw.png" alt="SageMaker" width="40" height="40"/> </a> <img src="https://auto.gluon.ai/stable/_static/AutogluonLogo.png" alt="AutoGluon" height="40"/> </a>
</p>



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
    <img width="450" src="/assets/hexagon_collisions.png"> 
</p>

## Repository Organization
- 00.Concept - Notebooks exploring hexagons and joining data
- 01.Data_Etl - Notebooks for data processing, joining and model data creation
- 02.Model - Notebooks used to create models
- 03.Analysis - Post-modeling analysis

## Getting Started
- Installation
```git clone https://github.com/jschmit-ds/capstone.git```

- [Requirements](/requirements.txt)
    - To use:
        - in a terminal, navigate to the directory of the downloaded repository
        - run this command ```pip install -r requirements.txt```
        - it is good practice to create a new environmnet prior to runing this code

- There are 3 data files needed to run this process
    - Crash data from TIMS years 2014 through 2021. A link to the website is provided [here](https://tims.berkeley.edu/)
        - can be downloaded from our repository as a [zip file](/X.Data/raw_data/TIMS_raw_crashes_downloads.zip)
        - credit: Transportation Injury Mapping System (TIMS), 
        Safe Transportation Research and Education Center, 
        University of California, Berkeley. 2022
    
    - LA County shape files
        - can be downloaded from our repository as a [zip file](/X.Data/raw_data/la_county_website_data.zip)
    
    - NOAA weather data downloaded from [here](https://www.ncei.noaa.gov/access/past-weather/)
        - can be download from our repository as a [zip file](/X.Data/weather/LA_weather_data_updated.csv.zip)
    
    - All other data is created and downloaded through the notebooks


## [Preprocessing Pipeline](/01.Data_Etl)
- Steps 01 - 05
    - download and pre-process data files
    - hexagons for LA County
    - LA County city shape file
    - TIMS accident data
    - road and intersection data
    - business location data
- Steps 11 - 14
    - further process data
    - create negative samples
    - create collision history
- Steps 20 - 23
    - Train/Test/Validate splits
    - join the data
    - output final modeling file
    - output 2022 out of time data for our dahsbaord
 - Steps 30 - 31
    - pre-modeling analysis
    - [pdf of pre-modeling univariates](/01.Data_Etl/pre-modeling_univariates.pdf)

![alt text](https://github.com/emoreno-hub/capstone/blob/main/assets/Data%20Model.jpg)

## [Machine Learning](/02.Model)
 - [GLMnet](/02.Model/GLMnet.ipynb)
 - [GBM](/02.Model/GBM.ipynb)
 - [AutoGluon](/02.Model/AutoGluon_Training.ipynb)

## Analysis
 - AUC calculations
 
 <p align="left" width="100%">
    <img width="350" src="/assets/out_of_time_auc.png "> 
</p>
 
 - [pdf of post-model modeling univeriates](/03.Analysis/validation_univariates.pdf)

<p align="left" width="100%">
    <img width="350" src="/assets/univariate.png "> 
</p>


## FAQ
