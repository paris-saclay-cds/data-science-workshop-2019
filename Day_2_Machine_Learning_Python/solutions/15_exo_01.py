from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import balanced_accuracy_score

X_breast, y_breast = load_breast_cancer(return_X_y=True)

X_breast_train, X_breast_test, y_breast_train, y_breast_test = train_test_split(
    X_breast, y_breast, stratify=y_breast, random_state=0,
    test_size=0.3)

pipe_breast = make_pipeline(StandardScaler(), SGDClassifier(max_iter=1000))
pipe_breast.fit(X_breast_train, y_breast_train)
y_pred = pipe_breast.predict(X_breast_test)
balanced_accuracy_score(y_breast_test, y_pred)
