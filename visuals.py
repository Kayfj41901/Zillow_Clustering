import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import wrangle_zillow 


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import env

df = wrangle_zillow.acquire()
df = wrangle_zillow.prepare_data(df)
train, validate, test = wrangle_zillow.split_zillow_data(df)

#under_two_bath = train[train.bathroomcnt_encoded==1]
#under_two_bath.logerror_encoded.value_counts(normalize=True)

#middle_bath = train[train.bathroomcnt_encoded==2]
#middle_bath.logerror_encoded.value_counts(normalize=True)

#over_four_bath = train[train.bathroomcnt_encoded==3]
#over_four_bath.logerror_encoded.value_counts()

def bathroom_pieplot():
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)

    data1 = [53, 47]
    labels1 = ['Inside IQR', 'Outside IQR']
    colors = sns.color_palette('coolwarm')[0:5]
    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('< 2 bath', fontdict = {'fontsize' : 14})


    data2 = [54, 46]
    labels2 = ['Inside IQR', 'Outside IQR']
    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title('2,3,4 bath', fontdict = {'fontsize' : 14})


    data3 = [59, 41]
    labels3 = ['Inside IQR', 'Outside IQR']
    ax3.pie(data3, labels = labels3, colors = colors, autopct='%.0f%%')
    ax3.set_title("> 4 bath", fontdict = {'fontsize' : 14})

    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(12,8)})
    plt.show()

def bathroomcnt_relplot():
    x = train.yearbuilt
    y = train.taxamount
    # Set size of figure
    plt.figure(figsize = (13,7))
    # Create scatterplot
    ax = sns.relplot(data=train, x= x, y= y, hue="logerror_encoded", col="bathroomcnt_encoded", col_wrap=3)
    # fit labels and legend
    plt.suptitle('Bathroom Count vs Log Error', fontsize = 20)
    plt.yticks(fontsize = 14)
    plt.ylabel('Log Error', fontsize = 16)


    plt.tight_layout() 
    plt.show()

#code for square feet pie plots to get percentages 
#a= train[train.finishedsquarefeet12_encoded==1]
#a.logerror_encoded.value_counts(normalize=True)

#b = train[train.finishedsquarefeet12_encoded==2]
#b.logerror_encoded.value_counts(normalize=True)

#c= train[train.finishedsquarefeet12_encoded==3]
#c.logerror_encoded.value_counts(normalize=True)

#d = train[train.finishedsquarefeet12_encoded==4]
#d.logerror_encoded.value_counts(normalize=True)

def SquareFeet_pieplot():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)

    data1 = [47, 53]
    labels1 = ['Inside IQR', 'Outside IQR']
    colors = sns.color_palette('coolwarm')[0:5]
    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('SqFt_code = 1', fontdict = {'fontsize' : 14})


    data2 = [50, 50]
    labels2 = ['Inside IQR', 'Outside IQR']
    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title('SqFt_code = 2', fontdict = {'fontsize' : 14})


    data3 = [51, 49]
    labels3 = ['Inside IQR', 'Outside IQR']
    ax3.pie(data3, labels = labels3, colors = colors, autopct='%.0f%%')
    ax3.set_title("SqFt_code = 3", fontdict = {'fontsize' : 14})

    data4 = [49, 51]
    labels4 = ['Inside IQR', 'Outside IQR']
    ax4.pie(data4, labels = labels4, colors = colors, autopct='%.0f%%')
    ax4.set_title("SqFt_code = 4", fontdict = {'fontsize' : 14})


    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(12,8)})
    plt.show()


def SquareFeet_relplot():
    x = train.yearbuilt
    y = train.taxamount
    # Set size of figure
    plt.figure(figsize = (13,7))
    # Create scatterplot
    ax = sns.relplot(data=train, x= x, y= y, hue="logerror_encoded", col="finishedsquarefeet12_encoded", col_wrap=2)
    # fit labels and legend
    plt.suptitle('Finished Square Feet vs Log Error', fontsize = 20)
    plt.yticks(fontsize = 14)
    plt.ylabel('Log Error', fontsize = 16)


    plt.tight_layout() 
    plt.show()

#code to get percent inside iqr for taxamount encoded 

#e= train[train.taxamount_encoded==1]
#e.logerror_encoded.value_counts(normalize=True)

#f= train[train.taxamount_encoded==2]
#f.logerror_encoded.value_counts(normalize=True)

#g= train[train.taxamount_encoded==3]
#g.logerror_encoded.value_counts(normalize=True)

#h= train[train.taxamount_encoded==4]
#h.logerror_encoded.value_counts(normalize=True)

def taxamount_pieplot():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)

    data1 = [43, 57]
    labels1 = ['Inside IQR', 'Outside IQR']
    colors = sns.color_palette('coolwarm')[0:5]
    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('Tax_Code=1', fontdict = {'fontsize' : 14})


    data2 = [49, 51]
    labels2 = ['Inside IQR', 'Outside IQR']
    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title('Tax_Code=2', fontdict = {'fontsize' : 14})


    data3 = [53, 47]
    labels3 = ['Inside IQR', 'Outside IQR']
    ax3.pie(data3, labels = labels3, colors = colors, autopct='%.0f%%')
    ax3.set_title("Tax_Code=3", fontdict = {'fontsize' : 14})

    data4 = [49, 51]
    labels4 = ['Inside IQR', 'Outside IQR']
    ax4.pie(data4, labels = labels4, colors = colors, autopct='%.0f%%')
    ax4.set_title("Tax_Code=4", fontdict = {'fontsize' : 14})


    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(12,8)})
    plt.show()

def taxamount_relplot():
    x = train.yearbuilt
    y = train.calculatedfinishedsquarefeet
    # Set size of figure
    plt.figure(figsize = (13,7))
    # Create scatterplot
    ax = sns.relplot(data=train, x= x, y= y, hue="logerror_encoded", col="taxamount_encoded", col_wrap=2)
    # fit labels and legend
    plt.suptitle('Tax Amount vs Log Error', fontsize = 20)
    plt.yticks(fontsize = 14)
    plt.ylabel('Log Error', fontsize = 16)


    plt.tight_layout() 
    plt.show()

#f = train[train.yearbuilt_encoded==1]
#f.logerror_encoded.value_counts(normalize=True)

#v = train[train.yearbuilt_encoded==2]
#v.logerror_encoded.value_counts(normalize=True)

#r = train[train.yearbuilt_encoded==3]
#r.logerror_encoded.value_counts(normalize=True)

#s = train[train.yearbuilt_encoded==4]
#s.logerror_encoded.value_counts(normalize=True)

def yearbuilt_pieplot():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)

    data1 = [38, 62]
    labels1 = ['Inside IQR', 'Outside IQR']
    colors = sns.color_palette('coolwarm')[0:5]
    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('1824-1952', fontdict = {'fontsize' : 14})


    data2 = [47, 53]
    labels2 = ['Inside IQR', 'Outside IQR']
    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title('1953-1969', fontdict = {'fontsize' : 14})


    data3 = [52, 48]
    labels3 = ['Inside IQR', 'Outside IQR']
    ax3.pie(data3, labels = labels3, colors = colors, autopct='%.0f%%')
    ax3.set_title("1970-1985", fontdict = {'fontsize' : 14})

    data4 = [58, 42]
    labels4 = ['Inside IQR', 'Outside IQR']
    ax4.pie(data4, labels = labels4, colors = colors, autopct='%.0f%%')
    ax4.set_title("1986-2015", fontdict = {'fontsize' : 14})

    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(12,8)})
    plt.show()

def yearbuilt_relplot():
    x = train.calculatedfinishedsquarefeet
    y = train.taxamount
    # Set size of figure
    plt.figure(figsize = (13,7))
    # Create scatterplot
    ax = sns.relplot(data=train, x= x, y= y, hue="logerror_encoded", col="yearbuilt_encoded", col_wrap=2)
    # fit labels and legend
    plt.suptitle('Year built vs Log Error', fontsize = 20)
    plt.yticks(fontsize = 14)
    plt.ylabel('Log Error', fontsize = 16)


    plt.tight_layout() 
    plt.show()
#code to get structure dollar per sqft percentages 
#w= train[train.structure_dollar_per_sqft_bin==1]
#w.logerror_encoded.value_counts(normalize=True)
#ww= train[train.structure_dollar_per_sqft_bin==2]
#ww.logerror_encoded.value_counts(normalize=True)
#ee= train[train.structure_dollar_per_sqft_bin==3]
#ee.logerror_encoded.value_counts(normalize=True)
#eee= train[train.structure_dollar_per_sqft_bin==4]
#eee.logerror_encoded.value_counts(normalize=True)

def per_sqft_pieplot():
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4)

    data1 = [42, 58]
    labels1 = ['Inside IQR', 'Outside IQR']
    colors = sns.color_palette('coolwarm')[0:5]
    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('$/sqft Q1', fontdict = {'fontsize' : 14})


    data2 = [49, 51]
    labels2 = ['Inside IQR', 'Outside IQR']
    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title('$/sqft Q2', fontdict = {'fontsize' : 14})


    data3 = [51, 49]
    labels3 = ['Inside IQR', 'Outside IQR']
    ax3.pie(data3, labels = labels3, colors = colors, autopct='%.0f%%')
    ax3.set_title("$/sqft Q3", fontdict = {'fontsize' : 14})

    data4 = [52, 48]
    labels4 = ['Inside IQR', 'Outside IQR']
    ax4.pie(data4, labels = labels4, colors = colors, autopct='%.0f%%')
    ax4.set_title("$/sqft Q4", fontdict = {'fontsize' : 14})


    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(12,8)})
    plt.show()

def price_sqft_relplot():
    x = train.yearbuilt
    y = train.taxamount
    # Set size of figure
    plt.figure(figsize = (13,7))
    # Create scatterplot
    ax = sns.relplot(data=train, x= x, y= y, hue="logerror_encoded", col="structure_dollar_per_sqft_bin", col_wrap=2)
    # fit labels and legend
    plt.suptitle('Structure Dollar Per Square Foot vs Log Error', fontsize = 20)
    plt.yticks(fontsize = 14)
    plt.ylabel('Log Error', fontsize = 16)


    plt.tight_layout() 
    plt.show()