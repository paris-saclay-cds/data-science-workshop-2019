categorical_columns = ['pclass', 'sex', 'embarked']
numerical_columns = ['age', 'sibsp', 'parch', 'fare']

categorical_titanic = titanic[categorical_columns]
numerical_titanic = titanic[numerical_columns]
