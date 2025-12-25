##_______________________________ code 4 _______________________________##

import numpy as np
from scipy import stats
from scipy.stats import ttest_rel
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import shapiro



#-----------------data----------------------
## ...............problem based...................
#drift type : gradual
file_path_merged_summary_grd = 'final results/merged_summary_grd.csv'
df_merged_summary_grd = pd.read_csv(file_path_merged_summary_grd)
#drift type : re-occurring
file_path_merged_summary_oc = 'final results/merged_summary_oc.csv'
df_merged_summary_oc = pd.read_csv(file_path_merged_summary_oc)
#drift type : sudden
file_path_merged_summary_sud = 'final results/merged_summary_sud.csv'
df_merged_summary_sud = pd.read_csv(file_path_merged_summary_sud)

# --------------------------------

## ...............domain based...................
#drift type : gradual
file_path_domain_based_mean_stdev_results_grd = 'final results/analysis/grd/domain_based_mean_stdev_results.csv'
df_domain_based_mean_stdev_results_grd = pd.read_csv(file_path_domain_based_mean_stdev_results_grd)
#drift type : re-occurring
file_path_domain_based_mean_stdev_results_oc = 'final results/analysis/occ/domain_based_mean_stdev_results.csv'
df_domain_based_mean_stdev_results_oc = pd.read_csv(file_path_domain_based_mean_stdev_results_oc)
#drift type : sudden
file_path_domain_based_mean_stdev_results_sud = 'final results/analysis/sudd/domain_based_mean_stdev_results.csv'
df_domain_based_mean_stdev_results_sud = pd.read_csv(file_path_domain_based_mean_stdev_results_sud)


metrics = ['BACC', 'Recall', 'Precision']

#==============================testing normal distribution with shapiro-wilk=======================================
#problem based - gradual
results_list_prblm_grd = []
for metric in metrics:
    before = df_merged_summary_grd[f'{metric} average not use']
    after = df_merged_summary_grd[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    
    # Normality test on differences
    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        # Normal → use paired t-test
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        # Non-normal → use Wilcoxon
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_prblm_grd.append({
        'N': len(before),
        'Drift type' : 'Gradual',
        'Based' : 'Problem',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('problem based - gradual')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_prblm_grd = pd.DataFrame(results_list_prblm_grd)
        


#problem based - re-occurring
results_list_prblm_oc = []
for metric in metrics:
    before = df_merged_summary_oc[f'{metric} average not use']
    after = df_merged_summary_oc[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    

    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_prblm_oc.append({
        'N': len(before),
        'Drift type' : 'Re-occurring',
        'Based' : 'Problem',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('problem based - re-occurring')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_prblm_oc = pd.DataFrame(results_list_prblm_oc)


#problem based - sudden
results_list_prblm_sud = []
for metric in metrics:
    before = df_merged_summary_sud[f'{metric} average not use']
    after = df_merged_summary_sud[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    
    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_prblm_sud.append({
        'N': len(before),
        'Drift type' : 'Sudden',
        'Based' : 'Problem',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('problem based - sudden')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_prblm_sud = pd.DataFrame(results_list_prblm_sud)


#domain based - gradual
results_list_dmn_grd = []
for metric in metrics:
    before = df_domain_based_mean_stdev_results_grd[f'{metric} average not use']
    after = df_domain_based_mean_stdev_results_grd[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    
    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_dmn_grd.append({
        'N': len(before),
        'Drift type' : 'Gradual',
        'Based' : 'Domain',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('domain based - gradual')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_dmn_grd = pd.DataFrame(results_list_dmn_grd)


#domain based - re-occurring
results_list_dmn_oc = []
for metric in metrics:
    before = df_domain_based_mean_stdev_results_oc[f'{metric} average not use']
    after = df_domain_based_mean_stdev_results_oc[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    
    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_dmn_oc.append({
        'N': len(before),
        'Drift type' : 'Re-occurring',
        'Based' : 'Domain',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('domain based - re-occurring')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_dmn_oc = pd.DataFrame(results_list_dmn_oc)


#domain based - sudden
results_list_dmn_sud = []
for metric in metrics:
    before = df_domain_based_mean_stdev_results_sud[f'{metric} average not use']
    after = df_domain_based_mean_stdev_results_sud[f'{metric} average use']
    diff = np.array(after) - np.array(before)
    
    stat, p_shapiro = stats.shapiro(diff)

    if p_shapiro > 0.05:
        dist_state = 'normal'
        t_stat, p_value = stats.ttest_rel(after, before)
        test_name = "Paired t-test"
    else:
        dist_state = 'not normal'
        try:
            t_stat, p_value = stats.wilcoxon(after, before)
        except ValueError as e:
            t_stat, p_value = np.nan, np.nan
            print(f"[{metric}] Wilcoxon test error: {e}")
        test_name = "Wilcoxon signed-rank test"


    if p_value < 0.05:
        test_result = 'Significant difference ✅'
    else:
        test_result = 'No significant difference ❌'

    
    results_list_dmn_sud.append({
        'N': len(before),
        'Drift type' : 'Gradual',
        'Based' : 'Problem',
        'metric' : metric,
        'Shapiro-Wilk p' : p_shapiro,
        'distribution state' : dist_state,
        'test name' : test_name,
        't_statistics' : t_stat,
        'test p_value' : p_value,
        'test result' : test_result
    })

    
    print('domain based - sudden')
    print(f"[{metric}]")
    print(f"  Shapiro-Wilk p = {p_shapiro:.6f} → {'normal' if p_shapiro > 0.05 else 'not normal'}")
    print(f"  {test_name} p = {p_value:.6f}")
    if p_value < 0.05:
        print(f"  📌 Significant difference ✅\n")
    else:
        print(f"  ℹ️ No significant difference ❌\n")
        

        
output_df_dmn_sud = pd.DataFrame(results_list_dmn_sud)
        



#==========================concat df===============================
df_all_results = pd.concat([
    output_df_prblm_grd, output_df_prblm_oc, output_df_prblm_sud,
    output_df_dmn_grd, output_df_dmn_oc, output_df_dmn_sud
], ignore_index=True)

df_all_results.to_csv('final results/statistics/satistics_all_results.csv', index=False, encoding='utf-8-sig')
