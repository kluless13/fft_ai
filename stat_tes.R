choose_statistical_test <- function(data_type, sample_size, independence, test_type, post_hoc=FALSE) {
  if (data_type == "numerical") {
    if (sample_size == 1) {
      if (test_type == "correlation") {
        return("Pearson's r")
      } else if (test_type == "difference") {
        return("One-Sample t-test")
      }
    } else if (sample_size == 2) {
      if (independence == "independent") {
        return("Two-Sample t-test (parametric) or Mann-Whitney U-test (non-parametric)")
      } else if (independence == "dependent") {
        return("Paired t-test (parametric) or Wilcoxon Signed-Rank test (non-parametric)")
      }
    } else if (sample_size > 2) {
      if (independence == "independent") {
        if (post_hoc) {
          return("Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)")
        }
        return("One-way ANOVA (parametric) or Kruskal-Wallis test (non-parametric)")
      } else if (independence == "dependent") {
        if (post_hoc) {
          return("Pairwise comparisons with adjustments (e.g., Bonferroni, Sidak, Holm-Bonferroni)")
        }
        return("Repeated Measures ANOVA (parametric) or Friedman test (non-parametric)")
      }
    }
  } else if (data_type == "categorical") {
    if (sample_size == 1) {
      if (test_type == "difference") {
        return("Chi-Square Goodness-of-Fit test")
      }
    } else if (sample_size == 2) {
      if (independence == "independent") {
        return("Chi-Square Test of Independence or Fisher's Exact Test (if expected frequencies are small)")
      } else if (independence == "dependent") {
        return("McNemar's Test")
      }
    } else if (sample_size > 2) {
      if (independence == "independent") {
        return("Logistic Regression or Multiple Logistic Regression")
      } else if (independence == "dependent") {
        return("GEE (Generalized Estimating Equations) or Multilevel Modeling (Mixed Models)")
      }
    }
  }
}

# Example usage
result <- choose_statistical_test("numerical", 3, "independent", NULL, post_hoc=TRUE)
print(result)  # Output: Tukey's HSD, Scheffe's test, Bonferroni (parametric); Dunn's test, Conover test (non-parametric)

