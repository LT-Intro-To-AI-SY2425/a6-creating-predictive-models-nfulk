# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
0.86, it tells me that the model is closely related to my data since it is a close value to 1.

2. Is your model accurate? Why or why not?
The model is pretty accurate as it gets close to a lot of the actual prices but it did miss big on the 18 year old car and doesn't take into account the fact that a car doesn't sell for negative value.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
They both give negative values.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
I think this is happening because the model doesn't take into account that the people selling gotta make a profit on their car and can't sell a car for negative value no matter how old or how many miles it has on it.