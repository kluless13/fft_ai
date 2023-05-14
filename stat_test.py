import streamlit as st

def choose_statistical_test(numerical_data, categorical_data, sample_size, independence, test_type):
    if numerical_data and not categorical_data:
        data_type = "numerical"
    elif not numerical_data and categorical_data:
        data_type = "categorical"
    elif numerical_data and categorical_data:
        data_type = "both"
    else:
        return "No valid data type selected"
    if data_type == "numerical":
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
                if post_hoc:
                    return "Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)"
                return "One-way ANOVA (parametric) or Kruskal-Wallis test (non-parametric)"
            elif independence == "dependent":
                if post_hoc:
                    return "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak, Holm-Bonferroni)"
                return "Repeated Measures ANOVA (parametric) or Friedman test (non-parametric)"
    elif data_type == "categorical":
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
    elif data_type == "both":
        if sample_size == 1:
            if test_type == "correlation":
                return "Bi-variate correlation"
            elif test_type == "difference":
                return "Chi-Square Goodness-of-Fit test"
        elif sample_size == 2:
            if independence == "independent":
                return "Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)"
            elif independence == "dependent":
                return "Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)"
        elif sample_size > 2:
            if independence == "independent":
                if post_hoc:
                    return "Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)"
                return "One-way MANOVA (parametric) or Kruskal-Wallis test (non-parametric)"
            elif independence == "dependent":
                if post_hoc:
                    return "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak, Holm-Bonferroni)"
                return "Repeated Measures MANOVA (parametric) or Friedman test (non-parametric)"

# Example usage:
result = choose_statistical_test("both", 3, "independent", "correlation", post_hoc=True)
print(result)  # Output: Tukey's HSD, Scheffe's test, Bonferroni (


st.title('Statistical Test Selector')

numerical_data = st.checkbox('Do you have numerical data?')
categorical_data = st.checkbox('Do you have categorical data?')
sample_size = st.number_input('Enter the sample size', min_value=1, value=1)
independence = st.selectbox('Is the sampling independent or dependent?', ('independent', 'dependent'))
test_type = st.selectbox('What type of test do you want to conduct?', ('correlation', 'difference'), index=0)

if st.button('Calculate'):
    result = choose_statistical_test(numerical_data, categorical_data, sample_size, independence, test_type)
    st.write('You should consider the following statistical test(s):', result)
