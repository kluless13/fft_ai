def choose_statistical_test(purpose, data_type_1, data_type_2=None):
    # Convert input strings to lowercase to ensure consistent comparisons
    purpose = purpose.lower()
    data_type_1 = data_type_1.lower()
    data_type_2 = data_type_2.lower() if data_type_2 else None

    # Check if the purpose is correlation or association
    if purpose == 'correlation' or purpose == 'association':
        # Case: Numerical vs. Numerical data
        if data_type_1 == 'numerical' and data_type_2 == 'numerical':
            return ["Pearson's correlation coefficient", "Spearman's rank correlation coefficient"]
        
        # Case: Categorical vs. Categorical data
        elif (data_type_1 == 'categorical' and data_type_2 == 'categorical') or \
             (data_type_2 == 'categorical' and data_type_1 == 'categorical'):
            return ["Chi-squared test", "Fisher's exact test (for small sample sizes)"]
        
        # Case: Numerical vs. Categorical data
        elif (data_type_1 == 'numerical' and data_type_2 == 'categorical') or \
             (data_type_2 == 'numerical' and data_type_1 == 'categorical'):
            return ["Point-biserial correlation coefficient"]

    # Check if the purpose is difference or comparison
    elif purpose == 'difference' or purpose == 'comparison':
        # Case: Numerical data
        if data_type_1 == 'numerical':
            # One sample
            if data_type_2 is None:
                return ["One-sample t-test", "One-sample Wilcoxon signed-rank test (non-parametric)"]
            
            # Two independent samples
            elif data_type_2 == 'independent':
                return ["Independent two-sample t-test", "Mann-Whitney U test (non-parametric)"]
            
            # Two paired samples
            elif data_type_2 == 'paired':
                return ["Paired t-test", "Wilcoxon signed-rank test (non-parametric)"]
            
            # More than two samples
            elif data_type_2 == 'multiple':
                return ["One-way ANOVA (post hoc tests: Tukey's HSD, Bonferroni, Scheffe's test)",
                        "Kruskal-Wallis test (non-parametric) (post hoc tests: Dunn's test, Conover's test)"]

        # Case: Categorical data
        elif data_type_1 == 'categorical':
            # Two independent samples
            if data_type_2 == 'independent':
                return ["Chi-squared test", "Fisher's exact test (for small sample sizes)"]
            
            # More than two samples
            elif data_type_2 == 'multiple':
                return ["Cochran's Q test (paired data) (post hoc tests: McNemar's test for pairwise comparisons)"]

    # Return an error message if the input is invalid
    else:
        return "Invalid input. Please check the purpose and data types."

# Example usage:
purpose = "correlation"
data_type_1 = "numerical"
data_type_2 = "categorical"

print(choose_statistical_test(purpose, data_type_1, data_type_2))
