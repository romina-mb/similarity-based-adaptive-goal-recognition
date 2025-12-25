##_______________________________ code 3 _______________________________##

import pandas as pd

def analyze_improvement(df, metric_name):
    len_df = len(df)
    imp_mean = df[f'{metric_name} improvement'].mean()
    imp_std = df[f'{metric_name} improvement'].std()
    imp_count = (df[f'{metric_name} improvement'] > 0).sum()
    imp_percent = (imp_count/len_df)*100
    drop_mean = df[df[f'{metric_name} improvement'] < 0][f'{metric_name} improvement'].mean()
    drop_count = (df[f'{metric_name} improvement'] < 0).sum()
    drop_percent = (drop_count/len_df)*100
    no_change_count = (df[f'{metric_name} improvement'] == 0).sum()
    no_change_percent = (no_change_count/len_df)*100
    return imp_mean, imp_std, imp_count, drop_count, imp_percent, drop_percent, drop_mean , no_change_count , no_change_percent


def analyze_improvement_domain_based(df, metric_name):
    len_df = len(df)
    imp_count = (df[f'{metric_name} improvement'] > 0).sum()
    imp_percent = (imp_count/len_df)*100
    drop_mean = df[df[f'{metric_name} improvement'] < 0][f'{metric_name} improvement'].mean()
    drop_count = (df[f'{metric_name} improvement'] < 0).sum()
    drop_percent = (drop_count/len_df)*100
    no_change_count = (df[f'{metric_name} improvement'] == 0).sum()
    no_change_percent = (no_change_count/len_df)*100
    return imp_count, drop_count, imp_percent, drop_percent, drop_mean , no_change_count , no_change_percent

##------------------------------gradual drift------------------------------------##
# file_path = 'final results/merged_summary_grd.csv'

##------------------------------re-occurring drift------------------------------------##
file_path = 'final results/merged_summary_oc.csv'

##------------------------------sudden drift------------------------------------##
# file_path = 'final results/merged_summary_sud.csv'

df = pd.read_csv(file_path)
df.head()


## -------------------------------------------BACC-----------------------------------------------------------------
# bacc_imp_rate_mean = df['BACC improvement ratio'].mean()

bacc_imp_mean, bacc_imp_std, bacc_imp_count, bacc_drop_count, bacc_imp_percent, bacc_drop_percent, bacc_drop_mean , bacc_no_change_count , bacc_no_change_percent = analyze_improvement(df , 'BACC')

# Finding the row with the most BACC improvement
max_bacc_imp_row = df.loc[df['BACC improvement'].idxmax()]
# Finding the row with the least BACC improvement
min_bacc_imp_row = df.loc[df['BACC improvement'].idxmin()]

## -------------------------------------------recall-----------------------------------------------------------------
# recall_imp_rate_mean = df['Recall improvement ratio'].mean()

recall_imp_mean, recall_imp_std, recall_imp_count, recall_drop_count, recall_imp_percent, recall_drop_percent, recall_drop_mean , recall_no_change_count , recall_no_change_percent = analyze_improvement(df , 'Recall')

# Finding the row with the most recall improvement
max_recall_imp_row = df.loc[df['Recall improvement'].idxmax()]
# Finding the row with the least recall improvement
min_recall_imp_row = df.loc[df['Recall improvement'].idxmin()]

## -------------------------------------------precision-----------------------------------------------------------------
# precision_imp_rate_mean = df['Precision improvement ratio'].mean()

precision_imp_mean, precision_imp_std, precision_imp_count, precision_drop_count, precision_imp_percent, precision_drop_percent, precision_drop_mean , precision_no_change_count , precision_no_change_percent = analyze_improvement(df , 'Precision')

# Finding the row with the most precision improvement
max_precision_imp_row = df.loc[df['Precision improvement'].idxmax()]
# Finding the row with the least precision improvement
min_precision_imp_row = df.loc[df['Precision improvement'].idxmin()]


#_______________________________________________group by domain____________________________________________________#
df['domain'] = df['Domain'].str.replace('-aaai$', '', regex=True)

df['domain'] = df['domain'].str.replace('rslt_use_grd_ol\\', 'gradual\\', regex=False)
# df['domain'] = df['domain'].str.replace('rslt_use_oc_ol\\', 're-occurring\\', regex=False)
# df['domain'] = df['domain'].str.replace('rslt_use_sud_ol\\', 'sudden\\', regex=False)


#mean
mean_df = df.groupby('domain')[['BACC average standard','BACC average not use','BACC average use', 'BACCDROP' , 'BACC improvement' ,'Recall average standard','Recall average not use' , 'Recall average use', 'Recall DROP' , 'Recall improvement' , 'Precision average standard' , 'Precision average not use' , 'Precision average use' , 'Precision DROP' , 'Precision improvement']].mean()

# Standard deviation
std_df = df.groupby('domain')[['BACC average standard','BACC average not use','BACC average use','BACC improvement' ,'Recall average standard','Recall average not use' , 'Recall average use', 'Recall improvement' , 'Precision average standard' , 'Precision average not use' , 'Precision average use' , 'Precision improvement']].std()

# Renaming std columns
std_df.columns = [col + ' std' for col in std_df.columns]

# Concatenating the mean and standard deviation
result_df = pd.concat([mean_df, std_df], axis=1).reset_index()

output_file_name = 'final results/analysis/grd/domain_based_mean_stdev_results.csv'
# output_file_name = 'final results/analysis/occ/domain_based_mean_stdev_results.csv'
# output_file_name = 'final results/analysis/sudd/domain_based_mean_stdev_results.csv'

result_df.to_csv(output_file_name, index=False)


len_result_df = len(result_df)
#-------------
#---precision---
precision_imp_count_domain, precision_drop_count_domain, precision_imp_percent_domain, precision_drop_percent_domain, precision_drop_mean_domain , precision_no_change_count_domain , precision_no_change_percent_domain = analyze_improvement_domain_based(result_df , 'Precision')

max_precision_imp_row_domain = result_df.loc[result_df['Precision improvement'].idxmax()]
min_precision_imp_row_domain = result_df.loc[result_df['Precision improvement'].idxmin()]

#-------------
#---recall---
recall_imp_count_domain, recall_drop_count_domain, recall_imp_percent_domain, recall_drop_percent_domain, recall_drop_mean_domain , recall_no_change_count_domain , recall_no_change_percent_domain = analyze_improvement_domain_based(result_df , 'Recall')

max_recall_imp_row_domain = result_df.loc[result_df['Recall improvement'].idxmax()]
min_recall_imp_row_domain = result_df.loc[result_df['Recall improvement'].idxmin()]

#-------------
#---BACC---
bacc_imp_count_domain, bacc_drop_count_domain, bacc_imp_percent_domain, bacc_drop_percent_domain, bacc_drop_mean_domain , bacc_no_change_count_domain , bacc_no_change_percent_domain = analyze_improvement_domain_based(result_df , 'BACC')

max_bacc_imp_row_domain = result_df.loc[result_df['BACC improvement'].idxmax()]
min_bacc_imp_row_domain = result_df.loc[result_df['BACC improvement'].idxmin()]


#_______________________________________________group by problem____________________________________________________#

#-------min max _ problems-------
analysis_min_max_df_all = pd.DataFrame({
    'max BACC improvement' : [max_bacc_imp_row['DomainFolder'] , max_bacc_imp_row['BACC improvement']],
    'min BACC improvement' : [min_bacc_imp_row['DomainFolder'] , min_bacc_imp_row['BACC improvement']],
    'max Recall improvement' : [max_recall_imp_row['DomainFolder'] , max_recall_imp_row['Recall improvement']],
    'min Recall improvement' : [min_recall_imp_row['DomainFolder'] , min_recall_imp_row['Recall improvement']],
    'max precision improvement' : [max_precision_imp_row['DomainFolder'] , max_precision_imp_row['Precision improvement']],
    'min precision improvement' : [min_precision_imp_row['DomainFolder'] , min_precision_imp_row['Precision improvement']],

}, index = ["Domain/problem", "amount"])


output_file_name_all = 'final results/analysis/grd/analysis_min_max_allp.csv'
# output_file_name_all = 'final results/analysis/occ/analysis_min_max_allp.csv'
# output_file_name_all = 'final results/analysis/sudd/analysis_min_max_allp.csv'

analysis_min_max_df_all.to_csv(output_file_name_all, index=False)


#-------mean count percent _ problems-------
mean_count_result_all = pd.DataFrame({
    'average BACC improvment' : [bacc_imp_mean],
    'BACC improvement std' : [bacc_imp_std],
    'BACC improvement count' : [bacc_imp_count],
    'BACC improvement percent' : [bacc_imp_percent],
    'average BACC drop' : [bacc_drop_mean],
    'BACC DROP count' : [bacc_drop_count],
    'BACC DROP percent' : [bacc_drop_percent],
    'BACC no change count' : [bacc_no_change_count],
    'BACC no change percent' : [bacc_no_change_percent],
    #--------
    'average Recall improvement' : [recall_imp_mean],
    'Recall improvement std' : [recall_imp_std],
    'Recall improvement count' : [recall_imp_count],
    'Recall improvement percent' : [recall_imp_percent],
    'average Recall drop' : [recall_drop_mean],
    'Recall DROP count' : [recall_drop_count],
    'Recall DROP percent' : [recall_drop_percent],
    'Recall no change count' : [recall_no_change_count],
    'Recall no change percent' : [recall_no_change_percent],
    #--------
    'average precision improvement' : [precision_imp_mean],
    'Precision improvement std' : [precision_imp_std],
    'precision improvement count' : [precision_imp_count],
    'precision improvement percent' : [precision_imp_percent],
    'average Precision drop' : [precision_drop_mean],
    'precision drop count' : [precision_drop_count],
    'precision drop percent' : [precision_drop_percent],
    'precision no change count' : [precision_no_change_count],
    'precision no change percent' : [precision_no_change_percent],
})


output_mean_count_res_all_file = 'final results/analysis/grd/output_mean_count_percent_all.csv'
# output_mean_count_res_all_file = 'final results/analysis/occ/output_mean_count_percent_all.csv'
# output_mean_count_res_all_file = 'final results/analysis/sudd/output_mean_count_percent_all.csv'

mean_count_result_all.to_csv(output_mean_count_res_all_file, index=False)

#----------------domain based-------------------#

#-------min max _ domains-------
analysis_min_max_df_domain = pd.DataFrame({
    'max bacc imp' : [max_bacc_imp_row_domain['domain'] , max_bacc_imp_row_domain['BACC improvement']],    
    'min bacc imp' : [min_bacc_imp_row_domain['domain'] , min_bacc_imp_row_domain['BACC improvement']],
    'max recall imp' : [max_recall_imp_row_domain['domain'] , max_recall_imp_row_domain['Recall improvement']],
    'min recall imp' : [min_recall_imp_row_domain['domain'] , min_recall_imp_row_domain['Recall improvement']],
    'max precision imp' : [max_precision_imp_row_domain['domain'],  max_precision_imp_row_domain['Precision improvement']],
    'min precision imp' : [min_precision_imp_row_domain['domain'] , min_precision_imp_row_domain['Precision improvement']],
}, index = ["Domain/problem", "amount"])

output_file_name_domain = 'final results/analysis/grd/analysis_min_max_domain.csv'
# output_file_name_domain = 'final results/analysis/occ/analysis_min_max_domain.csv'
# output_file_name_domain = 'final results/analysis/sudd/analysis_min_max_domain.csv'

analysis_min_max_df_domain.to_csv(output_file_name_domain, index=False)


#-------avg count percent _ domains-------
output_df_domain = pd.DataFrame({
    'bacc improvement count' : [bacc_imp_count_domain],
    'bacc improvement percent' : [bacc_imp_percent_domain],
    'bacc drop count' : [bacc_drop_count_domain],
    'bacc drop percent' : [bacc_drop_percent_domain],
    'bacc not change count' : [bacc_no_change_count_domain],
    'bacc no change percent' : [bacc_no_change_percent_domain],
    'average bacc drop' : [bacc_drop_mean_domain],
    'recall improvement count' : [recall_imp_count_domain],
    'recall improvement percent' : [recall_imp_percent_domain],
    'recall drop count' : [recall_drop_count_domain],
    'recall drop percent' : [recall_drop_percent_domain],
    'recall not change count' : [recall_no_change_count_domain],
    'recall no change percent' : [recall_no_change_percent_domain],
    'average recall drop' : [recall_drop_mean_domain],
    'precision improvement count' : [precision_imp_count_domain],
    'precision improvement percent' : [precision_imp_percent_domain],
    'precision drop count' : [precision_drop_count_domain],
    'precision drop percent' : [precision_drop_percent_domain],
    'precision not change count' : [precision_no_change_count_domain],
    'precision no change percent' : [precision_no_change_percent_domain],
    'average precision drop' : [precision_drop_mean_domain]
})


file_path_name = 'final results/analysis/grd/output_avg_count_percent_domain.csv'
# file_path_name = 'final results/analysis/occ/output_avg_count_percent_domain.csv'
# file_path_name = 'final results/analysis/sudd/output_avg_count_percent_domain.csv'

output_df_domain.to_csv(file_path_name, index=False)