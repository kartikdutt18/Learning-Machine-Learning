import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values
plt.scatter(x,y,color='blue')
plt.show()
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(x)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_poly,y)
x_grid=np.arange(min(x),max(x),0.05)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='blue')
plt.plot(x_grid,regressor.predict(poly_reg.fit_transform(x_grid)),color='red')
plt.show()
pred=regressor.predict(poly_reg.fit_transform(x_grid))
