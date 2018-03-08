import numpy as np
import pandas as pd
from sklearn import svm, neighbors
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df = df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1), dtype=np.float64)
y = np.array(df['class'], dtype=np.float64)

X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2)

clf1 = LinearRegression();
clf2 = svm.SVC();
clf3 = neighbors.KNeighborsClassifier()

clf1.fit(X_test, y_test)
print("Linear Accurecy", clf1.score(X_train, y_train))

clf2.fit(X_test, y_test)
print("SVM Accurecy ",clf2.score(X_train, y_train))

clf3.fit(X_test, y_test)
print("KN Accurecy ",clf3.score(X_train, y_train))

X_example = np.array([[8,6,4,3,5,9,3,1,1], [1,3,1,2,2,2,5,3,2]], dtype=np.float64)
predict_linear = clf1.predict(X_example)
predict_SVM = clf2.predict(X_example)
predict_KN = clf3.predict(X_example)

print("Linear Predic", predict_linear)
print("SVM Predic", predict_SVM)
print("KN Predic", predict_KN)