import re
import numpy as np
import os
import json
from feature_vector_functions import *
import yaml



#Definition of specific domains
unique_domain_name = ["easy-ipc-grid" , "sokoban" , "miconic" , "blocks-world"]


# Domain data path
base_folder = "./domains"

# Find all domain folders
domains = [d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))]

results = {}

# Processing each domain and problem category
for domain in domains:
    domain_path = os.path.join(base_folder, domain)
    
    # Find all problem categories in this domain
    problem_categories = [p for p in os.listdir(domain_path) if os.path.isdir(os.path.join(domain_path, p))]

    for category in problem_categories:
        category_path = os.path.join(domain_path, category)
        hyps_file = os.path.join(category_path, "hyps.dat")

        # Check if the hyps.dat file exists in the issue folder
        if os.path.exists(hyps_file):
            with open(hyps_file, "r") as f:
                goals = f.read().strip().split("\n")

            processed_goals = []
            goals_matches = []
            entity_list = []
            priority_list = []
            
            # # Processing each goal - applying the appropriate pattern and extracting parameters and matches
            for goal in goals:
                if domain not in unique_domain_name:
                    goal_match , processed_goal = extract_parameters_for_process_goal(goal , domain)
                    processed_goals.append(processed_goal)
                    goals_matches.append(goal_match)
                    
                elif domain == "miconic":
                    processed_goal_entity , processed_goal_priority , processed_goal_ent_pri = extract_parameters_for_process_goal(goal , domain)
                    entity_list.append(processed_goal_entity)
                    priority_list.append(processed_goal_priority)
                    goals_matches.append(processed_goal_ent_pri)
                    
                else:
                    processed_goal = extract_parameters_for_process_goal(goal , domain)
                    processed_goals.append(processed_goal)
                                
            
            #Extract the feature space
            if domain not in unique_domain_name:
                
                union_dictionary = calc_union_dict_dynamic(*processed_goals)
                feature_space = calc_feature_space_dynamic (union_dictionary)
                        
            elif domain == "miconic":
                hyps_entities = set_union(*entity_list)
                hyps_priorities = set_union(*priority_list)
                feature_space = create_feature_space(hyps_entities , hyps_priorities)                
            
            else:
                pass
            
            
            #Extract binary feature vector for each goal
            feature_vectors = []
            
            for goal_match in goals_matches:
                
                if domain not in unique_domain_name:
                    goal_feature_vector = create_boolian_feature_vector_dynamic(goal_match , feature_space)
                    feature_vectors.append(goal_feature_vector)
                
                
                elif domain == "miconic":
                    goal_feature_vector = create_priority_boolian_feature_vector(goal_match , feature_space)
                    feature_vectors.append(goal_feature_vector)
                        
                    
                else:
                    pass
                                  
            
            if domain not in unique_domain_name or domain == "miconic":
                results[f"{domain}/{category}"] = {f"goal_{i}": vec for i, vec in enumerate(feature_vectors)}
            else:    
                results[f"{domain}/{category}"] = {f"goal_{i}": goal for i, goal in enumerate(processed_goals)}

            
output_file = "./processed_goals.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)


# print(f"✅ process done successfully and results saved in file '{output_file}' ")
