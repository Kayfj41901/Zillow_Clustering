
# ignore warnings
import os
import warnings
warnings.filterwarnings("ignore")

# Wrangling
import pandas as pd
import numpy as np

import sklearn.metrics

# Exploring
import scipy.stats as stats

# Visualizing
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import env
import visuals
from scipy.stats import f_oneway

import wrangle_zillow
import scipy.stats as stats

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

pd.options.display.max_rows = 100 

# default pandas decimal number display format
pd.options.display.float_format = '{:20,.2f}'.format

















np.set_printoptions(suppress=True)