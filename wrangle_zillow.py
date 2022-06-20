import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import env

#prop.* prop refers to the alias we gave the properties_2017 table 
#Left joins allow me to keep all my properties whether or not the information is there
#the join query in the middle identifies the distinct transaction date associated with max_transactiondate


query = '''
SELECT
    prop.*,
    predictions_2017.logerror,
    predictions_2017.transactiondate,
    air.airconditioningdesc,
    arch.architecturalstyledesc,
    build.buildingclassdesc,
    heat.heatingorsystemdesc,
    landuse.propertylandusedesc,
    story.storydesc,
    construct.typeconstructiondesc
FROM properties_2017 prop
JOIN (
    SELECT parcelid, MAX(transactiondate) AS max_transactiondate
    FROM predictions_2017
    GROUP BY parcelid
) pred USING(parcelid)
JOIN predictions_2017 ON pred.parcelid = predictions_2017.parcelid
                      AND pred.max_transactiondate = predictions_2017.transactiondate
LEFT JOIN airconditioningtype air USING (airconditioningtypeid)
LEFT JOIN architecturalstyletype arch USING (architecturalstyletypeid)
LEFT JOIN buildingclasstype build USING (buildingclasstypeid)
LEFT JOIN heatingorsystemtype heat USING (heatingorsystemtypeid)
LEFT JOIN propertylandusetype landuse USING (propertylandusetypeid)
LEFT JOIN storytype story USING (storytypeid)
LEFT JOIN typeconstructiontype construct USING (typeconstructiontypeid)
WHERE prop.latitude IS NOT NULL
  AND prop.longitude IS NOT NULL
  AND transactiondate <= '2017-12-31'
'''

#drop duplex, planned unit development, quadruplex, triplex, cluster home, cooperative, commercial 
def filter_properties(df):
    filter_cols = ['Single Family Residential', 'Mobile Home', 'Manufactured, Modular, Prefabricated Homes', 'Residential General', 'Townhouse']
    df = df[df['propertylandusedesc'].isin(filter_cols)]
    return df

def drop_units(df):
    df.drop(df.index[df['unitcnt'] == 2], inplace=True)
    df.drop(df.index[df['unitcnt'] == 4], inplace=True)
    df.drop(df.index[df['unitcnt'] == 3], inplace=True)
    return df

def drop_outliers(df):
    df.drop(df[df['taxvalue_taxamount'] > 1000].index, inplace = True)
    df.drop(df[df['structuretax_taxamount'] > 300].index, inplace = True)
    df.drop(df[df['Sqft_structuretax'] > 5].index, inplace = True)
    df.drop(df[df['Landtax_taxamount'] > 1000].index, inplace = True)
    df.drop(df[df['Structuretax_landtax'] > 30].index, inplace = True)
    return df


def handle_missing_values(df, prop_required_column = .5):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    return df

def drop_columns(df):
    df.drop(columns=['transactiondate', 'parcelid', 'unitcnt', 'id', 'heatingorsystemdesc', 'buildingqualitytypeid', 'heatingorsystemtypeid',  'propertyzoningdesc', 'propertylandusedesc', 'propertycountylandusecode'], inplace=True)
    return df

def feature_engineer(df):
    df['age'] = 2017 - df.yearbuilt
    df['logerror'] = df['logerror'].abs()
    df['Sqft_age'] = df.calculatedfinishedsquarefeet/df.age
    df['Sqft_structuretax'] = df.calculatedfinishedsquarefeet/df.structuretaxvaluedollarcnt
    df['Sqft_taxvalue'] = df.calculatedfinishedsquarefeet/df.taxvaluedollarcnt
    df['Sqft_landtax'] = df.calculatedfinishedsquarefeet/df.landtaxvaluedollarcnt
    df['Sqft_taxamount'] = df.calculatedfinishedsquarefeet/df.taxamount
    df['age_structuretax'] = df.age/df.structuretaxvaluedollarcnt
    df['age_taxvalue'] = df.age/df.taxvaluedollarcnt
    df['age_landtax'] = df.age/df.landtaxvaluedollarcnt
    df['age_taxamount'] = df.age/df.taxamount
    df['Structuretax_taxvalue'] = df.structuretaxvaluedollarcnt/df.taxvaluedollarcnt
    df['Structuretax_landtax'] = df.structuretaxvaluedollarcnt/df.landtaxvaluedollarcnt
    df['Landtax_taxamount'] = df.landtaxvaluedollarcnt/df.taxamount
    df['structuretax_taxamount'] = df.structuretaxvaluedollarcnt/df.taxamount
    df['taxvalue_landtax'] = df.taxvaluedollarcnt/df.landtaxvaluedollarcnt
    df['taxvalue_taxamount'] = df.taxvaluedollarcnt/df.taxamount
    return df 

def handle_outliers(df):
    df.drop(df[df['bathroomcnt'] == 0].index, inplace = True)
    df.drop(df[df['finishedsquarefeet12'] > 15000].index, inplace = True)
    df.drop(df[df['regionidzip'] > 150000].index, inplace = True)
    df.drop(df[df['taxvaluedollarcnt'] > 5000000].index, inplace = True)
    df.drop(df[df['landtaxvaluedollarcnt'] > 5000000].index, inplace = True)
    df.drop(df[df['taxamount'] > 20000].index, inplace = True)
    return df

def split_zillow_data(df):
    '''
    This function performs split on zillow data
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test

def prepare_data(df):
    df = filter_properties(df)
    df = drop_units(df)
    df = handle_missing_values(df)
    df = drop_columns(df)
    df = df.dropna()
    df = feature_engineer(df)
    df = drop_outliers(df)
    return df

def acquire():
    if os.path.exists('zillow.csv'):
        df = pd.read_csv('zillow.csv')
    else:
        database = 'zillow'
        url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
        df = pd.read_sql(query, url)
        df.to_csv('zillow.csv', index=False)
    return df