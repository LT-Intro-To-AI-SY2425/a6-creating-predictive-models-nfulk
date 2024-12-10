import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

# Load the data
data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values.reshape(-1, 1)  # Reshape to 2D array
y = data["Blood Pressure"].values

# Split the data into training and testing datasets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression().fit(x_train, y_train)

# Find the coefficient, bias, and r-squared value
coefficient = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
r_squared = round(model.score(x_train, y_train), 2)

# Print out the linear equation and r-squared value
print(f"Linear Equation: Blood Pressure = {coefficient} * Age + {intercept}")
print(f"R-squared Value (Training Data): {r_squared}")

'''
**********TEST THE MODEL**********
'''

# Get the predicted y values for the x_test values
y_pred = model.predict(x_test)

# Round the predicted values
y_pred = np.round(y_pred, 2)

# Test the model by looping through all of the values in the x_test dataset
print("\nTesting Linear Model with Testing Data:")
for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual}, Predicted: {predicted}")

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
y_pred = model.predict(x)
# Plot the training data, testing data, and line of best fit
plt.scatter(x_train, y_train, color='blue', label='Training Data', alpha=0.7)
plt.scatter(x_test, y_test, color='green', label='Testing Data', alpha=0.7)
plt.plot(x, model.predict(x), color='red', label='Line of Best Fit', linewidth=2)

# Add labels, title, and legend
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Age vs Blood Pressure (Training and Testing Results)")
plt.legend()

# Show the plot
plt.show()