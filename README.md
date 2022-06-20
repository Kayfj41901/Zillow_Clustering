### Project Description

The purpose of this project is to find the drivers of log error and use this insight to create a model (or multiple models) that outperforms the baseline model for logerror. At the end of this process, I conclude there are no features that significantly 'drive' logerror. I do have a recommendation based on my research; it does not provide a path to finding a new 'driver' of logerror but does give a sensible option for fixing the root issue. My report includes all steps of the data science pipeline.

### Goals

Project goals include. . . 

- Construct an ML Regression model that predicts log error of Single Unit Properties using attributes of the properties.
- Find the key drivers of logerror for single family properties.
- Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.


Keeping in mind that the reasoning behind the goals is to . . 

- Make recommendations on what works or doesn't work in predicting log error.

### Initial Hypothesis

- Newer properties have less variance of log error than newer properties 
- Properties with lower tax value have greater variance in log error. 
- Different types of tax value information is the best option for identifying log error 

### Data Dictionary

0   bathroomcnt                   50592 non-null  float64
 1   bedroomcnt                    50592 non-null  float64
 2   calculatedbathnbr             50592 non-null  float64
 3   calculatedfinishedsquarefeet  50592 non-null  float64
 4   finishedsquarefeet12          50592 non-null  float64
 5   fips                          50592 non-null  float64
 6   fullbathcnt                   50592 non-null  float64
 7   latitude                      50592 non-null  float64
 8   longitude                     50592 non-null  float64
 9   lotsizesquarefeet             50592 non-null  float64
 10  propertylandusetypeid         50592 non-null  float64
 11  rawcensustractandblock        50592 non-null  float64
 12  regionidcity                  50592 non-null  float64
 13  regionidcounty                50592 non-null  float64
 14  regionidzip                   50592 non-null  float64
 15  roomcnt                       50592 non-null  float64
 16  yearbuilt                     50592 non-null  float64
 17  structuretaxvaluedollarcnt    50592 non-null  float64
 18  taxvaluedollarcnt             50592 non-null  float64
 19  assessmentyear                50592 non-null  float64
 20  landtaxvaluedollarcnt         50592 non-null  float64
 21  taxamount                     50592 non-null  float64
 22  censustractandblock           50592 non-null  float64
 23  logerror                      50592 non-null  float64
 24  age                           50592 non-null  float64
 25  Sqft_age                      50592 non-null  float64
 26  Sqft_structuretax             50592 non-null  float64
 27  Sqft_taxvalue                 50592 non-null  float64
 28  Sqft_landtax                  50592 non-null  float64
 29  Sqft_taxamount                50592 non-null  float64
 30  age_structuretax              50592 non-null  float64
 31  age_taxvalue                  50592 non-null  float64
 32  age_landtax                   50592 non-null  float64
 33  age_taxamount                 50592 non-null  float64
 34  Structuretax_taxvalue         50592 non-null  float64
 35  Structuretax_landtax          50592 non-null  float64
 36  Landtax_taxamount             50592 non-null  float64
 37  structuretax_taxamount        50592 non-null  float64
 38  taxvalue_landtax              50592 non-null  float64
 39  taxvalue_taxamount            50592 non-null  float64

### Project Planning

This project will complete all steps of the data science pipeline to include:

Data Acquisition : 
- Run a query to pull the zillow information from SQL into the jupyter notebook 

Data Preparation: 
- Filtered properties by propertylanduse desc to only include: 
    -Single Family Residential 
    -Mobile Home 
    -Manufactured
    -Modular 
    -Prefabricated Homes 
    -Residential General 
    -Townhouse 
- Dropped units over count 'one'
- Dropped all columns that had 50% or more missing values 
- Dropped columns: 
    - transactiondate: feature used to filter data, will not use in modeling 
    - parcelid: unique identifier, will not be useful for modeling 
    - unitcnt: only one value per row: 1; will not be useful for modeling 
    - id: unique identifier, will not be useful for modeling 
    - heatingorsystemdesc, buildingqualitytypeid, heatingorsystemtypeid, propertyzoningdesc, propertylandusedesc, propertycountylandusecode: over 20 percent null values - did not want to impute or drop null values
- Dropped all rows with null values: at this point all rows were missing less than 5% of the data 
- Created New Features: 
    - age: 2017 - yearbuilt 
    - logerror: absolute value of logerror
    - sqft_age: calculatedfinishedsquarefeet/age 
    - sqft_structuretax: calculatedfinishedsquarefeet/structuretaxvaluedollarcnt
    - Sqft_taxvalue: calculatedfinishedsquarefeet/taxvaluedollarcnt
    - Sqft_landtax: calculatedfinishedsquarefeet/landtaxvaluedollarcnt
    - Sqft_taxamount: calculatedfinishedsquarefeet/taxamount
    - age_structuretax: age/structuretaxvaluedollarcnt
    - age_taxvalue: age/taxvaluedollarcnt 
    - age_landtax: age/landtaxvaluedollarcnt
    - age_taxamount: age/taxamount
    - structuretax_taxvalue: structuretaxvaluecnt/taxvaluedollarcnt
    - structuretax_landtax: structuretaxvaluedollarcnt/landtaxvaluedollarcnt
    - Landtax_taxamount: landtaxvaluedollarcnt/taxamount
    - structuretax_taxamount: structuretaxvaluedollarcnt/ taxamount 
    - taxvalue_landtax: taxvaluedollarcnt/ landtaxvaluedollarcnt 
    - taxvalue_taxamount: taxvaluedollarcnt/ taxamount
- Started with (77380, 68) ended with (50616, 40)
- Retain 65% of data 

Exploratory Data Analysis: 
These questions will be answered through charts/visuals:
- Is there a relationship between taxvalue_taxamount feature and logerror? 
- Is there a relationship between structuretax_taxamount feature and logerror? 
- Is there a relationship between Sqft_structuretax feature and logerror? 
- Is there a relationship between landtax_taxamount feature and logerror? 
- Is there a relationship between Structuretax_landtax and logerror? 


Statistics: Statistical tests will be performed to test these hypotheses: 
-There is a relationship between taxvalue_taxamount feature and logerror? 
-There is a relationship between structuretax_taxamount feature and logerror? 
-There is a relationship between Sqft_structuretax feature and logerror? 
-There is a relationship between landtax_taxamount feature and logerror? 
-There is a relationship between Structuretax_landtax and logerror? 

Modeling: 

-  3 Linear OLS Models 


Model Evaluation: 
- Model 1  was shown to be more accurate

### Key Findings

- While we can conclude from this report that some features correlate with logerror, or show up as a feature importance on RFE, the relationships are too weak to classify any of them as a 'driver' of logerror. 

### Recommendations

- Upon review of the clusters, I noticed certain clusters have a significantly higher than average mean log error value. Until more drivers of error can be identified and a better model created, I suggest posting a 'range zestimate.' Instead of valueing a property as a specific number, I would say 'based on other properties in this area, we estimate this property will sell between '280,000 and 320,000.' This will help manage consumer's expectations and secure the reputation of the company.

### How to reproduce this project

Download wrangle.py, visuals.py, and Regressionprojectestimatinghomevalue.ipynb. In addition you will need your own env.py to access the codeup database. Then run Regressionprojectestimatinghomevalue.ipynb.
