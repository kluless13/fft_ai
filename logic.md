Start
|
V
What type of data? (data_type_1, data_type_2)
|
+--> Numerical (data_type_1)
|   |
|   V
|   Sample size (1 or more than 1)?
|   |
|   +--> 1
|   |   |
|   |   V
|   |   Type of test (Correlation or Difference)?
|   |   |
|   |   +--> Correlation: Pearson's r
|   |   |
|   |   +--> Difference: One-Sample t-test
|   |
|   +--> 2
|   |   |
|   |   V
|   |   Independence of sampling (Independent or Dependent)?
|   |   |
|   |   +--> Independent: Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)
|   |   |
|   |   +--> Dependent: Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)
|   |
|   +--> More than 2
|       |
|       V
|       Independence of sampling (Independent or Dependent)?
|       |
|       +--> Independent: One-way ANOVA (parametric) or Kruskal-Wallis test (non-parametric)
|       |
|       +--> Dependent: Repeated Measures ANOVA (parametric) or Friedman test (non-parametric)
|
+--> Categorical (data_type_2)
|   |
|   V
|   Sample size (1 or more than 1)?
|   |
|   +--> 1
|   |   |
|   |   V
|   |   Type of test (Correlation or Difference)?
|   |   |
|   |   +--> Difference: Chi-Square Goodness-of-Fit test
|   |
|   +--> 2
|   |   |
|   |   V
|   |   Independence of sampling (Independent or Dependent)?
|   |   |
|   |   +--> Independent: Chi-Square Test of Independence or Fisher's Exact Test (if expected frequencies are small)
|   |   |
|   |   +--> Dependent: McNemar's Test
|   |
|   +--> More than 2
|       |
|       V
|       Independence of sampling (Independent or Dependent)?
|       |
|       +--> Independent: Logistic Regression or Multiple Logistic Regression
|       |
|       +--> Dependent: GEE (Generalized Estimating Equations) or Multilevel Modeling (Mixed Models)
|
+--> Both (data_type_1 and data_type_2)
    |
    V
    Sample size (1 or more than 1)?
    |
    +--> 1
    |   |
    |   V
    |   Type of test (Correlation or Difference)?
    |   |
    |   +--> Correlation: Bi-variate correlation
    |   |
    |   +--> Difference: Chi-Square Goodness-of-Fit test
    |
    +--> 2
    |   |
    |   V
    |   Independence of sampling (Independent or Dependent)?
    |   |
    |   +--> Independent: Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)
    |   |
    |   +--> Dependent: Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)
    |   +--> More than 2
    |       |
    |       V
    |       Independence of sampling (Independent or Dependent)?
    |       |
    |       +--> Independent: One-way MANOVA (parametric) or Kruskal-Wallis test (non-parametric)
    |       |
    |       +--> Dependent: Repeated Measures MANOVA (parametric) or Friedman test (non-parametric)
    |
    +--> No Valid Data Type: Please select a valid data type
End
