import os
import pandas as pd

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import cross_val_score

titanic = pd.read_csv(os.path.join('datasets', 'titanic3.csv'))
target = titanic['survived']
titanic = titanic[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]

categorical_columns = ['pclass', 'sex', 'embarked']
numerical_columns = ['age', 'sibsp', 'parch', 'fare']

categorical_pipeline = make_pipeline(
    SimpleImputer(strategy='constant'), OneHotEncoder(handle_unknown='ignore')
)
numerical_pipeline = make_pipeline(
    StandardScaler(), SimpleImputer()
)

preprocessor = make_column_transformer(
    (categorical_pipeline, categorical_columns),
    (numerical_pipeline, numerical_columns)
)

pipe = make_pipeline(preprocessor, RandomForestClassifier(n_estimators=100))
print(pipe.fit(titanic, target).score(titanic, target))

print(cross_val_score(pipe, titanic, target, cv=5))
