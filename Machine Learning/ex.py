import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *

x=([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y=[35,40,50,55,65,70,75,85,90,95]

model=LinearRegression()
model.fit(x,y)

pred1=model.predict([[5]])
pred2=model.predict([[7.5]])
pred3=model.predict([[12]])

print("The Prediction for 5 is:",pred1)
print("The Prediction for 7.5 is:",pred2)
print("The Prediction for 12 is:",pred3)

print("The COEF is:",model.coef_)
print("The Intercept is:",model.intercept_)

print("The R² is:",model.score(x,y))