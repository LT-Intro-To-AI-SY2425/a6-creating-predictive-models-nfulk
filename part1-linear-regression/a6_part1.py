import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coefficient = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
r_squared = round(model.score(x, y), 2)


# Print out the linear equation and r squared value
print(f"Linear Equation: Blood Pressure = {coefficient} * Age + {intercept}")
print(f"R-squared Value: {r_squared}") 
# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction
age_43 = np.array([[43]])
predicted_bp = round(model.predict(age_43)[0], 2)
print(f"Predicted Blood Pressure for a 43-year-old: {predicted_bp}")
# Create the model in matplotlib and include the line of best fit
y_pred = model.predict(x)
plt.scatter(x, y, label="Data Points", alpha=0.7)
plt.plot(x, y_pred, color="red", label="Line of Best Fit", linewidth=2)
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Age vs Blood Pressure with Line of Best Fit")
plt.legend()
plt.show()