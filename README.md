### Project Description

The purpose of this project is to create a model (or multiple models) that outperforms the baseline model for predicting home values. At the end of this process, I discover one new insight into how a feature affects model performance. I hope my final recommendation is valuable in helping our data science team develop a very accurate model by end of quarter. My report includes all steps of the data science pipeline.

### Goals

Project goals include. . . 

- Construct an ML Regression model that predicts propery tax assessed values of Single Family Properties using attributes of the properties.
- Find the key drivers of property value for single family properties.
- Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.
- Provide information about what state and county the data has been pulled from

Keeping in mind that the reasoning behind the goals is to . . 

- Make recommendations on what works or doesn't work in predicting home values.

### Initial Hypothesis

- Given the same location, older properties have less tax value than newer properties 
- Given the same location, properties with more bedrooms have a higher tax value than homes with fewer bedrooms. 
- Given the same location, properties with more bathrooms have a higher tax value than homes with fewer bathrooms. 

### Data Dictionary

bedroomcnt = number of bedrooms

bathroomcnt = number of bathrooms to include half baths

calculatedfinishedsquarefeet = square feet of property 

fips(changed to 'location') = numerical designator for county. This column was renamed to 'location' and the numerical identifiers were mapped to 'Orange' for Orange County 'Ventura' for Ventura County and 'LA' for LA county.

taxvaluedollarcnt = property tax value

yearbuilt = the year the home was built

### Project Planning

This project will complete all steps of the data science pipeline to include:

Data Acquisition : 
- Run a query to pull the zillow information from SQL into the jupyter notebook 

Data Preparation: 
- Sorted Values in Descending order and dropped (first) row with 2018 transaction 
- Dropped columns propertylandusedesc, transactiondate (only joined into original data to filter by 'single family homes', and 'transaction date 2017 homes')
- Dropped all null values 
- Dropped outliers using Q1/Q3 plus/minus (1.5 * IQR) for bedroom count, bathroom count, square feet, and tax value dollar count 
- Converted fips, yearbuilt, taxvaluedollarcnt, calculatedfinishedsquarefeet, and bedroomcnt to datatype integer 

Exploratory Data Analysis: 
These questions will be answered through charts/visuals:
- Why do some properties have a much higher value than others when they are located so close to each other? 
- Which has a greater influence on home value: number of bathrooms or number of bedrooms?
- Do more bathrooms equate to a higher property value?
- Do more bedrooms equate to a higher property value? 

Statistics: Statistical tests will be performed to test these hypotheses: 
- Given the same location, older properties have less tax value than newer properties 
- Given the same location, properties with more bedrooms have a higher tax value than homes with fewer bedrooms. 
- Given the same location, properties with more bathrooms have a higher tax value than homes with fewer bathrooms. 

Modeling: 
- Linear Models 
- NonLinear Models 

Model Evaluation: 
- The non linear models were shown to be more accurate than the OLS linear model

### Key Findings

- Homes with fewer than 2 bathrooms in Ventura and Orange County have a noticeably different relationship with year built and property tax value when compared with homes that have 2 or more bathrooms.  Homes with fewer than 3 bathrooms in LA have a noticeably different relationship with year built and property tax value when compared with homes that have 3 or more bathrooms. 

### Recommendations

- I recommend subsetting the final data analysis by county and then again at fewer than two bathrooms for Orange and Ventura counties and at fewer than 3 bathrooms in LA. 

### How to reproduce this project

Download wrangle.py, visuals.py, and Regressionprojectestimatinghomevalue.ipynb. In addition you will need your own env.py to access the codeup database. Then run Regressionprojectestimatinghomevalue.ipynb.
