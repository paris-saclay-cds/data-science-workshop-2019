from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

cat_encoded = OneHotEncoder(sparse=False).fit_transform(categorical_titanic)
num_normalized = StandardScaler().fit_transform(numerical_titanic)
