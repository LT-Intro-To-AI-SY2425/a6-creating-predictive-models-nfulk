import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

print("Values of x (Independent Variables):")
print(x[:5])  
print("\nValues of y (Dependent Variable):")
print(y[:5]) 
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler()
# Step 3: Transform the data
x = scaler.fit_transform(x)

print("\nStandardized Values of x (Independent Variables):")
print(x[:5])
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# Step 5: Fit the data
model = linear_model.LogisticRegression()
# Step 6: Create a LogsiticRegression object and fit the data
model.fit(x_train, y_train)
# Step 7: Print the score to see the accuracy of the model
accuracy = model.score(x_test, y_test)
print(f"\nModel Accuracy: {accuracy:.2f}")
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
print("\n***************")
print("Testing Results:")

y_pred = model.predict(x_test)
for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual}, Predicted: {predicted}")