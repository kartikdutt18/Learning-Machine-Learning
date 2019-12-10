import pandas as pd
import numpy as np
dataset=pd.read_csv('Churn_Modelling.csv')
x=dataset.iloc[:,3:13].values
y=dataset.iloc[:,13].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lb_x=LabelEncoder()
x[:,1]=lb_x.fit_transform(x[:,1])
lb_x1=LabelEncoder()
x[:,2]=lb_x1.fit_transform(x[:,2])
ohe=OneHotEncoder(categorical_features=[1])
x=ohe.fit_transform(x).toarray()
x=x[:,1:]
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.fit_transform(x_test)
import keras
from keras.models import Sequential
from keras.layers import Dense
clas=Sequential()
clas.add(Dense(output_dim=6,init='uniform',activation='relu',input_dim=11))
clas.add(Dense(output_dim=6,init='uniform',activation='relu'))
clas.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))
clas.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
clas.fit(x_train,y_train,batch_size=15,nb_epoch=100)
pred=clas.predict(x_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pred)