##_______________________________ code 1 _______________________________##

import csv
import pandas as pd
import numpy as np
import statistics
import re
import os


def calc_evaluation_measure(csv_file_path):
    
    # Read the file and select the real_goal and result columns
    csv_df = pd.read_csv(csv_file_path, usecols=['Real_Goal', 'Results'])

    real_pred_list = list(csv_df.itertuples(index=False, name=None))
    first_elements = [item[0] for item in real_pred_list]
    total_goal_count = len(set(first_elements))
        
    all_bacc_list = []
    all_precision_list = []
    all_recall_list = []

    # Calculating metrics for each trace
    for record in real_pred_list:
        real_goal = int(record[0])
        predicted_goal = [int(x) for x in record[1].split('/') if x.strip() != '']

        bacc = BACC_func(total_goal_count , predicted_goal , real_goal)
        precision = precision_func(predicted_goal , real_goal)
        recall = recall_func(predicted_goal , real_goal)
        
        all_bacc_list.append(bacc)
        all_precision_list.append(precision)
        all_recall_list.append(recall)

    return all_bacc_list, all_precision_list, all_recall_list
    


# tp: True goal correctly detected
# fp: False goals detected as goals
# tn: Goals that were not part of the predictions (not a goal and correctly detected as not a goal)
# fn: True goal not detected

def BACC_func(total , predicted_goals , real_goal):  
    tp = 0
    fp = 0
    for goal in predicted_goals:
        if goal == real_goal:
            tp += 1
        else:
            fp += 1
    
    fn = 1 - tp

    # total is the number of all goals
    tn = total - tp - fp - fn

    tpr = tp/(tp + fn)
    tnr = tn/(tn + fp)
    bacc = (tpr + tnr)/2
    
    return bacc


def calc_average(data_list):
    avg_data = np.nanmean(data_list)
    return avg_data

    
def precision_func(predicted_goals , real_goal):
    tp = 0
    fp = 0
    for goal in predicted_goals:
        if goal == real_goal:
            tp += 1
        else:
            fp += 1
    
    precision = tp/(tp + fp)
    return precision
    

def recall_func(predicted_goals , real_goal):  
    tp = 0
    fp = 0
    for goal in predicted_goals:
        if goal == real_goal:
            tp += 1
        else:
            fp += 1
    
    fn = 1 - tp

    recall = tp/(tp + fn)
    return recall


def calc_measure_DROP(avg_list1 , avg_list2):
    measure_DROP = avg_list1 - avg_list2
    return measure_DROP

def calc_measure_improvement(avg_list1 , avg_list2):
    measure_improvement = avg_list1 - avg_list2
    return measure_improvement

# #improvement ratio
# def calc_improvement_ratio(measure_improvement, measure_DROP):
#     if measure_DROP ==0 :
#         return np.nan
#     else:
#         imp_ratio = measure_improvement / measure_DROP
#         return imp_ratio


def standard_deviation_func(data_list):
    stndev = statistics.stdev(data_list)
    return stndev


##==========Evaluation of each input file=============##
def sys_evaluation(csv_file_path_input , csv_file_path_output):
        
    input_df = pd.read_csv(csv_file_path_input, usecols=['Real_Goal', 'Results'])

    all_bacc_list, all_precision_list, all_recall_list = calc_evaluation_measure(csv_file_path_input)

    average_bacc = calc_average(all_bacc_list)
    bacc_stdev = standard_deviation_func(all_bacc_list)


    average_recall = calc_average(all_recall_list)
    recall_stdev = standard_deviation_func(all_recall_list)

    average_precision = calc_average(all_precision_list)
    precision_stdev = standard_deviation_func(all_precision_list)
    


    output_df = pd.DataFrame({
        'Real_Goal': input_df['Real_Goal'],
        'Results': input_df['Results'],
        'BACC': all_bacc_list,
        'Precision': all_precision_list,
        'Recall': all_recall_list
    })

    output_df.to_csv(csv_file_path_output, index=False)

    return output_df , average_bacc , average_recall , average_precision , bacc_stdev , recall_stdev , precision_stdev
    

# ==============================================================================

def sys_evaluation_compare(file_path0_std_sys, output_file_path0_std_sys, file_path1_use, output_file_path1_use, file_path2_not_use, output_file_path2_not_use , output_file_path_compare):
    
    df_std , BACC_avg_std , Recall_avg_std , precision_avg_std , BACC_stdev_std , Recall_stdev_std , precision_stdev_std = sys_evaluation(file_path0_std_sys , output_file_path0_std_sys)
    df_use , BACC_avg_use , Recall_avg_use , precision_avg_use , BACC_stdev_use , Recall_stdev_use , precision_stdev_use= sys_evaluation(file_path1_use , output_file_path1_use)
    df_not_use , BACC_avg_not_use , Recall_avg_not_use , precision_avg_not_use , BACC_stdev_not_use , Recall_stdev_not_use , precision_stdev_not_use= sys_evaluation(file_path2_not_use , output_file_path2_not_use)
    
    bacc_DROP = calc_measure_DROP(BACC_avg_std,BACC_avg_not_use)
    bacc_improvement = calc_measure_improvement(BACC_avg_use,BACC_avg_not_use)
    # bacc_improvement_ratio = calc_improvement_ratio(bacc_improvement,bacc_DROP)
  
    
    recall_DROP = calc_measure_DROP(Recall_avg_std,Recall_avg_not_use)
    recall_improvement = calc_measure_improvement(Recall_avg_use,Recall_avg_not_use)
    # recall_improvement_ratio = calc_improvement_ratio(recall_improvement,recall_DROP)


    precision_DROP = calc_measure_DROP(precision_avg_std,precision_avg_not_use)
    precision_improvement = calc_measure_improvement(precision_avg_use,precision_avg_not_use)
    # precision_improvement_ratio = calc_improvement_ratio(precision_improvement,precision_DROP)
    

    match = re.search(r'/([^/]+)_([^_]+)_-openloop', file_path1_use)

    if match:
        domain = match.group(1)
        problem = match.group(2)

    output_df = pd.DataFrame({
        'Domain' : [domain],
        'Problem name' : [problem],
        'BACC average standard' : BACC_avg_std ,
        'BACC stdev standard' : BACC_stdev_std ,
        'BACC average not use' : BACC_avg_not_use,
        'BACC stdev not use' : BACC_stdev_not_use,
        'BACC average use' : BACC_avg_use,
        'BACC stdev use' : BACC_stdev_use,
        'BACCDROP' : bacc_DROP,
        'BACC improvement' : bacc_improvement,
        # 'BACC improvement ratio' : bacc_improvement_ratio,
        'Recall average standard' : Recall_avg_std,
        'Recall stdev standard' : Recall_stdev_std,
        'Recall average not use' : Recall_avg_not_use,
        'Recall stdev not use' : Recall_stdev_not_use,
        'Recall average use' : Recall_avg_use,
        'Recall stdev use' : Recall_stdev_use,
        'Recall DROP' : recall_DROP,
        'Recall improvement' : recall_improvement,
        # 'Recall improvement ratio' : recall_improvement_ratio,
        'Precision average standard' : precision_avg_std,
        'Precision stdev standard' : precision_stdev_std,
        'Precision average not use' : precision_avg_not_use,
        'Precision stdev not use' : precision_stdev_not_use,
        'Precision average use' : precision_avg_use,
        'Precision stdev use' : precision_stdev_use,
        'Precision DROP' : precision_DROP,
        'Precision improvement' : precision_improvement,
        # 'Precision improvement ratio' : precision_improvement_ratio
    })
    
    
    output_df.to_csv(output_file_path_compare, index= False)
    

# # # =======================================================

##------------------------------gradual drift------------------------------------##
folder_std = 'gradual/rslt_std_grd_ol'
folder_use = 'gradual/rslt_use_grd_ol'
folder_not_use = 'gradual/rslt_not_grd_ol'

output_base_folder = 'final results/sys evaluation_grd_ol'

##------------------------------re-occurring drift------------------------------------##
# folder_std = 'occ/rslt_std_oc_ol'
# folder_use = 'occ/rslt_use_oc_ol'
# folder_not_use = 'occ/rslt_not_oc_ol'

# output_base_folder = 'final results/sys evaluation_oc_ol'

##------------------------------sudden drift------------------------------------##
# folder_std = 'sudden/rslt_std_sud_ol'
# folder_use = 'sudden/rslt_use_sud_ol'
# folder_not_use = 'sudden/rslt_not_sud_ol'

# output_base_folder = 'final results/sys evaluation_sud_ol'

files_std = sorted(os.listdir(folder_std))



counter = 0


for filename in files_std:
    file_path0_std_sys = os.path.join(folder_std, filename)
    
    base_name = filename.replace('.csv', '')
    base_name_output = filename.replace('_-openloop_per50.0.csv', '')
    
    file_path1_use = os.path.join(folder_use, base_name + '_True.csv')
    file_path2_not_use = os.path.join(folder_not_use, base_name + '_False.csv')
    
    
    output_folder = os.path.join(output_base_folder, base_name_output)
    os.makedirs(output_folder, exist_ok=True)
    
    output_file_path0_std_sys = os.path.join(output_folder, 'std_sys.csv')
    output_file_path1_use = os.path.join(output_folder, 'use.csv')
    output_file_path2_not_use = os.path.join(output_folder, 'not_use.csv')
    output_file_compare_path = os.path.join(output_folder, 'compare.csv')
    
    sys_evaluation_compare(file_path0_std_sys, output_file_path0_std_sys, file_path1_use, output_file_path1_use, file_path2_not_use, output_file_path2_not_use, output_file_compare_path)
    