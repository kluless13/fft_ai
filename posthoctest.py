def choose_posthoc_test(data_type_1, data_type_2, sample_size, independence):
    if data_type_1 == "numerical" and data_type_2 == "None":
        if sample_size > 2:
            if independence == "independent":
                return "Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)"
            elif independence == "dependent":
                return "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak, Holm-Bonferroni)"

    elif data_type_1 == "categorical" and data_type_2 =="None":
        if sample_size > 2:
            return "Post hoc analysis with adjusted residuals"

    elif data_type_1 == "numerical" and data_type_2 == "categorical":
        if sample_size > 2:
            return "Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak)"

    else:
        return "No valid data type selected"
