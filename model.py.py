from statsmodels.stats.proportion import proportions_ztest

def ab_test(group1, group2):
    success = [group1.sum(), group2.sum()]
    total = [group1.count(), group2.count()]

    z_stat, p_value = proportions_ztest(success, total)
    
    return z_stat, p_value