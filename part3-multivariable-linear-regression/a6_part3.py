import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

print(f"Coefficients: Miles: {coef[0]}, Age: {coef[1]}")
print(f"Intercept: {intercept}")
print(f"R-Squared: {r_squared}")

#Loop through the data and print out the predicted prices and the 
#actual prices
predicted_prices = model.predict(xtest)
predicted_prices = np.around(predicted_prices, 2)

for i in range(len(xtest)):
    miles, age = xtest[i]
    actual_price = ytest[i]
    predicted_price = predicted_prices[i]
    print(f"Miles: {miles}, Age: {age}, Actual Price: {actual_price}, Predicted Price: {predicted_price}")