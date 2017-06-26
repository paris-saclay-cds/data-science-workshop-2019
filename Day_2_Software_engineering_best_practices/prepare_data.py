import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')

step = 190
for idx, sl in enumerate(np.arange(step, data.shape[0], step)):
    sub_data = data.iloc[sl - step:sl]
    sub_data.to_csv('data/spectra_{}.csv'.format(idx))
