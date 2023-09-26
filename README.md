# MICE-Algorithm (Multiple Imputation by Chained Equations)
### A good approach for handling missing values before applying machine-learning algorithms.

In this algorithm, first, instead of each missing value, we put the average value of the missing value's feature, then in each step, by evaluating the model whose missing value's feature is the target, we predict the missing value.
