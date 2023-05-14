def choose_statistical_test(data_type_1, data_type_2, sample_size, independence, test_type):
    if data_type_1 == "numerical" and data_type_2 is None:
        if sample_size == 1:
            if test_type == "correlation":
                return "Pearson's r"
            elif test_type == "difference":
                return "One-Sample t-test"
        elif sample_size == 2:
            if independence == "independent":
                return "Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)"
            elif independence == "dependent":
                return "Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)"
        elif sample_size > 2:
            if independence == "independent":
                return "One-way ANOVA (parametric) or Kruskal-Wallis test (non-parametric)"
            elif independence == "dependent":
                return "Repeated Measures ANOVA (parametric) or Friedman test (non-parametric)"

    elif data_type_1 == "categorical" and data_type_2 is None:
        if sample_size == 1:
            if test_type == "difference":
                return "Chi-Square Goodness-of-Fit test"
        elif sample_size == 2:
            if independence == "independent":
                return "Chi-Square Test of Independence or Fisher's Exact Test (if expected frequencies are small)"
            elif independence == "dependent":
                return "McNemar's Test"
        elif sample_size > 2:
            if independence == "independent":
                return "Logistic Regression or Multiple Logistic Regression"
            elif independence == "dependent":
                return "GEE (Generalized Estimating Equations) or Multilevel Modeling (Mixed Models)"

    elif data_type_1 == "numerical" and data_type_2 == "categorical":
        if sample_size == 1:
            if test_type == "correlation":
                return "Bivariate correlation"
            elif test_type == "difference":
                return "Chi-Square Goodness-of-Fit test"
        elif sample_size == 2:
            if independence == "independent":
                return "Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)"
            elif independence == "dependent":
                return "Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)"
        elif sample_size > 2:
            if independence == "independent":
                return "One-way MANOVA (parametric) or Kruskal-Wallis test (non-parametric)"
            elif independence == "dependent":
                return "Repeated Measures MANOVA (parametric) or Friedman test (non-parametric)"

    else:
        return "No valid data type selected"
