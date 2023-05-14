def choose_posthoc_test(data_type_1, data_type_2, statistical_test):
    posthoc_tests = {
        "One-way ANOVA": "Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)",
        "Repeated Measures ANOVA": "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak, Holm-Bonferroni)",
        "Chi-Square Test of Independence": "Post hoc analysis with adjusted residuals",
        "Logistic Regression": "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak)",
        "One-way MANOVA": "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak)",
        "Repeated Measures MANOVA": "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak)",
    }

    if statistical_test in posthoc_tests:
        return posthoc_tests[statistical_test]
    else:
        return "No post hoc test necessary"