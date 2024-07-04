# Python code on sklearn linear regression example  
  
# Importing required libraries  
import numpy as np  
import matplotlib.pyplot as plt
from sklearn import linear_model  
from sklearn.datasets import load_diabetes  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import mean_squared_error, r2_score  
  
# Loading the sklearn diabetes dataset  
X, Y = load_diabetes(return_X_y=True)  
  
# Taking only one feature to perform simple linear regression  
X = X[:,8].reshape(-1,1)  
  
# Splitting the dependent and independent features of the dataset into training and testing dataset  
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 0.3, random_state = 10 )  
  
# Creating an instance for the linear regression model of sklearn  
lr = linear_model.LinearRegression()  
  
# Training the model by passing the dependent and independent features of the training dataset  
lr.fit( X_train, Y_train )  
  
# Creating an array of predictions made by the model for the unseen or test dataset  
Y_pred = lr.predict( X_test )  
  
# The value of the coefficients for the independent feature through the multiple regression model  
print("Value of the oefficients: \n", lr.coef_)  
  
# The value of the mean squared error  
print(f"Mean square error: {mean_squared_error( Y_test, Y_pred)}")  
  
# The value of the coefficient of determination, i.e., R-square score of the model  
print(f"Coefficient of determination: {r2_score( Y_test, Y_pred )}")  
  
# Plotting the output  
plt.scatter(X_test, Y_test, color = "black", label = "original data")  
plt.plot(X_test, Y_pred, color = "blue", linewidth=3, label = "regression line")  
plt.xlabel("Independent Feature")  
plt.ylabel("Target Values")  
plt.title("Simple Linear Regression") 
plt.show()
