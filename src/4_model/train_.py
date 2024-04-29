"""Entrenamiendo de un modelo de regresión usando sklear"""

import glob
import json
import os.path
import pandas as pd
from sklearn.feature_extraction import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

CONFIG_FILE = "config/config.json"

with open(CONFIG_FILE, "r", encoding ="utf-8") as file:
    config = json.load(file)

