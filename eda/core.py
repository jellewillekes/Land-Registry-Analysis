import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from upsetplot import UpSet


def exploratory_analysis(data):
    # Check data types:
    print(data.dtypes)
    data.dtypes
    data.dtypes.to_csv('../results/dtypes.csv')
    # Check data completeness:
    print(data.count())
    variables_null = data.isnull().sum()


