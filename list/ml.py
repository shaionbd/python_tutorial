import math, datetime
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import style

style.use('ggplot')

# df = quandl.get("WIKI/GOOGL")
# df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
# df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
#
# df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]
#
# df.to_csv('stock.csv')
df = pd.read_csv('stock.csv')
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
forecast_out = int(math.ceil(0.001*len(df))) # 4days

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume', 'label']]

X = np.array(df.drop(['label'], 1))
X_lately = X[-forecast_out:]
y = np.array(df['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
accurecy = clf.score(X_test, y_test)
predict = clf.predict(X_lately)
print(predict)



