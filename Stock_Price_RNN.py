import pandas as pd
dataset=pd.read_csv('Google_Stock_Price_Train.csv')
import matplotlib.pyplot as plt
import numpy as np
train_set=dataset.iloc[:,1:2].values
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler(feature_range=(0,1))
tr_sc=scal.fit_transform(train_set)
x_train=[]
y_train=[]
for i in range(60,1258):
    x_train.append(tr_sc[i-60:i,0])
    y_train.append(tr_sc[i,0])
x_train,y_train=np.array(x_train),np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
from keras.layers import Dense,LSTM,Dropout
from keras.models import Sequential
regressor=Sequential()
regressor.add(LSTM(units = 128, return_sequences = True, input_shape = (x_train.shape[1], 1)))
regressor.add(Dropout(p=0.2))
regressor.add(LSTM(units=128,return_sequences=True))
regressor.add(Dropout(p=0.2))
regressor.add(LSTM(units=128,return_sequences=True))
regressor.add(Dropout(p=0.2))
regressor.add(LSTM(units=128,return_sequences=True))
regressor.add(Dropout(p=0.2))
regressor.add(LSTM(units = 128))
regressor.add(Dropout(p=0.2))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam',loss='mean_squared_error')
regressor.fit(x_train,y_train,epochs=128,batch_size=32)
dataset_test = pd.read_csv('Google_Stock_Price_Test.csv')
real_stock_price = dataset_test.iloc[:, 1:2].values
dataset_total = pd.concat((dataset['Open'], dataset_test['Open']), axis = 0)
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = scal.transform(inputs)
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = regressor.predict(X_test)
predicted_stock_price = scal.inverse_transform(predicted_stock_price)
plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()
import math
from sklearn.metrics import mean_squared_error
rmse = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))
