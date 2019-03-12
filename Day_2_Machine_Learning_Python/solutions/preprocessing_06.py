import os
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.compose import make_column_transformer

adult = pd.read_csv(os.path.join('datasets', 'adult_openml.csv'))

y = adult['class']
X = adult.drop(columns=['class', 'fnlwgt', 'capitalgain', 'capitalloss'])

col_cat = ['workclass', 'education', 'marital-status', 'occupation',
           'relationship', 'race', 'native-country', 'sex']
col_num = ['age', 'hoursperweek']

pipe_cat = OneHotEncoder(handle_unknown='ignore')
pipe_num = KBinsDiscretizer()

preprocessor = make_column_transformer(
    (col_cat, pipe_cat, ), (col_num, pipe_num)
)

X_encoded = preprocessor.fit_transform(X)
X_encoded[:10]
