# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
Went from 0.89 to 0.65, without the StandardScaler, the model becomes less accurate because it struggles to compare features like Age and EstimatedSalary properly since they are on very different scales.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
0.89 which is close enough because it's close to the value of 1.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
It was fairly accurate throughout the model only messing up a little bit.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
No
