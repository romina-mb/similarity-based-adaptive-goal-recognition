from feature_vector_functions import *
import json
import pandas as pd
import csv


#_______________________functions_____________________________

def select_goals_stable(category_goals, n):
    """
    Select the last n goals from the list of goals
    - If there are fewer than n goals, it selects all.
    - If there are more, it only selects the last n.
    """
    goal_keys = list(category_goals.keys())
    total_goals = len(goal_keys)

    return goal_keys[-n:] if total_goals > n else goal_keys

#_______________________functions - end_____________________________


with open("./processed_goals.json", "r") as f:
    data = json.load(f)   #type == dict

#Choosing new goals
num_new_goals = 3  # Number of goals selected as new goals
new_goals = {}

for category, goals in data.items():
    new_goals[category] = select_goals_stable(goals, num_new_goals)


output_file = "./selected_new_goals.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(new_goals, f, ensure_ascii=False, indent=4)
    

#Calculating the similarity of the newly selected goals to other goals
similarity_matrix = {}

for category, goals in new_goals.items():
    similarity_matrix[category] = {}
    domain = category.split("/")[0]

    for new_goal in goals:
        similarity_matrix[category][new_goal] = {}

        for existing_goal, existing_vector in data[category].items():

            if existing_goal != new_goal and existing_goal not in goals:
                similarity_matrix[category][new_goal][existing_goal] = similarity_calculator(data[category][new_goal], existing_vector , domain)



output_file = "./similarity_matrix.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(similarity_matrix, f, ensure_ascii=False, indent=4)
    

rows = []
for category, goals in similarity_matrix.items():
    for new_goal, similarities in goals.items():
        for existing_goal, similarity_score in similarities.items():
            rows.append([category, new_goal, existing_goal, similarity_score])

df = pd.DataFrame(rows, columns=["Category", "New Goal", "Existing Goal", "Similarity"])
df.to_csv("./goal_similarity.csv", index=False)


# Setting similar goals for new targets
filtered_similarity_matrix = {}
all_similarities = {}

for category, goals in similarity_matrix.items():
    domain = category.split("/")[0]

    threshold_dict = {}
    for new_goal, similarities in goals.items():
        all_similarities = list(similarities.values())
    
        match domain:
            case "blocks-world" | "easy-ipc-grid" | "sokoban":
                threshold = min(all_similarities)  # Consider the lowest value as the threshold.
                
            case "intrusion-detection" | "rovers" | "zeno-travel" | "depots" | "driverlog" | "logistics" | "ferry" | "satellite" | "dwr" | "miconic":
                threshold = max(all_similarities)  # Consider the highest value as the threshold.
        
        threshold_dict[new_goal] = threshold


    filtered_similarity_matrix[category] = {}

    for new_goal, similarities in goals.items():
        if domain in ["easy-ipc-grid", "blocks-world" , "sokoban"]:  
            # Selecting items whose similarity value is less than the threshold
            filtered_goals = {existing_goal: similarity for existing_goal, similarity in similarities.items() if similarity <= threshold_dict[new_goal]}
        elif domain in ["miconic" , "intrusion-detection", "rovers" , "zeno-travel", "depots" , "driverlog" , "logistics" , "ferry" , "satellite" , "dwr"]:
            # Selecting items whose similarity value is greater than the threshold
            filtered_goals = {existing_goal: similarity for existing_goal, similarity in similarities.items() if similarity >= threshold_dict[new_goal]}
        else:
            filtered_goals = {}  #If the domain has no specific condition, nothing will be selected.

        if filtered_goals:  # If at least one value is valid
            filtered_similarity_matrix[category][new_goal] = filtered_goals



with open("./filtered_similarity.json", "w") as f:
    json.dump(filtered_similarity_matrix, f, indent=4)


rows = []

for category, goals in filtered_similarity_matrix.items():
    for new_goal, similarities in goals.items():
        for existing_goal, similarity_score in similarities.items():
            rows.append([category, new_goal, existing_goal, similarity_score])

df = pd.DataFrame(rows, columns=["Category", "New Goal", "Existing Goal", "Similarity"])
df.to_csv("./filtered_goal_similarity.csv", index=False)
