# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?
This model is more effective because it uses train-test splitting, which allows us to evaluate its performance on unseen data, ensuring better generalization and avoiding overfitting.

2. What does the R squared coefficient tell you about the model?
The R-squared value shows how well the line fits the data, telling us how much of the change in blood pressure can be explained by a person's age, a value closer to 1 means the line fits really well.

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.
In terms of just based off this data the model is accurate. The model's accuracy is supported by the close match between predicted and actual values, a high R-squared value, and alignment with the American Heart Association's blood pressure categories.