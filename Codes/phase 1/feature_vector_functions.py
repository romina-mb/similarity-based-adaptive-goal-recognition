import re
import numpy as np
from itertools import product
from sklearn.metrics import jaccard_score

#=======================================similarity function==================================================================

#---Jaccard similarity calculation function---
def jaccard_similarity_func(object1D1 , object1D2):
    return jaccard_score(object1D1, object1D2)



#---Euclidean distance calculation function---
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point2) - np.array(point1))



#---Levenshtein distance calculation function---
def levenshtein_distance(str1, str2):

    len1, len2 = len(str1), len(str2)
    
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    
    # Distance calculation
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0  # The characters are equal.
            else:
                cost = 1  # The characters are different.
            
            dp[i][j] = min(dp[i - 1][j] + 1,        # Delete
                           dp[i][j - 1] + 1,        # Insertion
                           dp[i - 1][j - 1] + cost) # Replacement
    
    return dp[len1][len2]


##            function for calculating similarity based on the domain             ##

def similarity_calculator(object1 , object2 , domain):
    match domain:
        case "blocks-world":
            similarity = levenshtein_distance(object1 , object2)
        case "sokoban":
            similarity = calculate_distances_sokoban(object1 , object2)
        case "easy-ipc-grid":
            similarity = euclidean_distance(object1 , object2)
        case "intrusion-detection" | "rovers" | "zeno-travel" | "depots" | "driverlog" | "logistics" | "ferry" | "satellite" | "dwr" | "miconic": 
            similarity = jaccard_similarity_func(object1 , object2)
    
    
    return similarity


#=======================================general function==================================================================


# Function to find target patterns based on domain
def pattern_finder(domain_name):
    match domain_name:
        case "easy-ipc-grid" :
            return r'\d+'
        case "blocks-world" :
            return r"\((\w+)\s+(\w+)(?:\s+(\w+))?\)"
        case "sokoban":
            return r"\(at\s+(box\d+)\s+f(\d+)-(\d+)f\)"
        case "miconic":
            return r"\(served\s+(\w+)\)"
        #--------------------------------------------
        case "intrusion-detection" | "rovers" | "zeno-travel" | "depots" | "driverlog" | "logistics" | "ferry" | "satellite" | "dwr":
            return r"\(([\w\s*-]+)\)"
        
        case _:
            return "Pattern not found for this domain."
    
        
# Pattern matching function
def pattern_matcher(goal_string , domain_name):
    pattern = pattern_finder(domain_name)
    matches = re.findall(pattern, goal_string)
    
    if domain_name == "easy-ipc-grid":
        return [int(num) for num in matches]
    else:
        return matches


#Function to separate words in a pattern
def split_match_state(matches):
    split_matches = [match.split() for match in matches]
    return split_matches



# The aggregation function of sets
def set_union(*the_set):
    union_list = set()
    for test_set in the_set:
        union_list = union_list.union(test_set)

    return union_list
     


#Function to extract the parameters of each key in the target and generate a dictionary for it
def extract_parameters_dynamic(matches):
    data = {}
    for match in matches:
        key = match[0]
        parameters_count = len(match) - 1
        if key not in data:
            data[key] = {i: set() for i in range(1, parameters_count + 1) }  # ایجاد کلیدهای داینامیک

        for i in range(1, parameters_count + 1):
            data[key][i].add(match[i])

    return data



#Dynamic aggregation function of sets in specific keys in dictionaries
def calc_union_dict_dynamic(first_data_dictionary, *data_dictionaries):
    union_dict = first_data_dictionary.copy()
    
    for dictionary in data_dictionaries:
        for key in dictionary:
            if key not in union_dict:
                union_dict[key] = {sub_key: set() for sub_key in dictionary[key]}
            
            for sub_key in dictionary[key]:
                union_dict[key][sub_key] = set_union(union_dict[key].get(sub_key, set()), dictionary[key][sub_key])

    return union_dict



#Function to generate dynamic feature space from dictionary 
def calc_feature_space_dynamic(union_dictionary):
    feature_space_dict = {}

    for key in union_dictionary:
        minor_feature_space = create_feature_space_dynamic(key, union_dictionary[key])        
        feature_space_dict[key] = minor_feature_space

    final_feature_space = set()

    for key in feature_space_dict:
        final_feature_space = set_union(feature_space_dict[key], final_feature_space)


    return list(final_feature_space)




# Function to create dynamic feature space
def create_feature_space_dynamic(key , dictionary):
    array = np.array([list(values) for values in dictionary.values()], dtype=object)

    # Using product to create possible combinations
    result = [','.join(combo) for combo in product(*array)]

    #Add key to all elements
    final_result = [f"{key}({item})" for item in result]

    return final_result


#Function to create binary dynamic feature vector
def create_boolian_feature_vector_dynamic(matches, feature_space):
    feature_vector = [0] * len(feature_space)
        
    formatted_strings = [f"{item[0]}({','.join(item[1:])})" for item in matches]

    for feature_name in formatted_strings:  
        if feature_name in feature_space:
            index = feature_space.index(feature_name)
            feature_vector[index] = 1

    return feature_vector


#=======================================function for miconic==================================================================

#Function to create feature space
def create_feature_space(entities_list , locations_list):
    
    feature_space = [f"{entity}@{location}" for entity in entities_list for location in locations_list]
    return feature_space


#Priority extraction function
def extract_priorities(matches):
    entities = []
    priorities = []
    entity_priority = []
    
    pri_num = 1
    
    for match in matches:
        entities.append(match)
        priorities.append(str(pri_num))
        entity_priority.append((match , str(pri_num)))
        pri_num += 1
    
    return entities, priorities , entity_priority


#Function to generate binary feature vector based on priority
def create_priority_boolian_feature_vector(matches , feature_space):
    feature_vector = [0] * len(feature_space)

    for entity, priority in matches:
        feature_name = f"{entity}@{priority}"
        if feature_name in feature_space:
            index = feature_space.index(feature_name)
            feature_vector[index] = 1
    return feature_vector


#=======================================function for blocks-world==================================================================

#Word generation function from goal descriptions
def create_word(goal_state):
    
    goal_word = [0] * (len(goal_state)+1)

    index = 0

    for item in goal_state:
        if item[0] == "ON":
            if index == 0:
                goal_word[index] = item[1]
            
            index +=1   
            goal_word[index] = item[2]
            
            
    word = ""
    for letter in goal_word:
        
        if isinstance(letter , str):
            word = word+letter
    
    return word


#=======================================function for sokoban==================================================================

#Dictionary generation function to assign locations to the appropriate key
def dict_generator(matchesList):
    result = {}
    for item in matchesList:
        key = item[0]
        values = list(map(int, item[1:]))
        result[key] = values
       
    return result
        

#Calculating Euclidean distance between locations - specific to the Sokoban domain
def calculate_distances_sokoban(dict1, dict2):
    # Extracting common keys
    common_keys = dict1.keys() & dict2.keys()
      
    distance_sum = 0
    
    for key in common_keys:
        point1 = dict1[key]
        point2 = dict2[key]

        distance = euclidean_distance(point1, point2)
        distance_sum += distance
        
    return distance_sum



#=======================================function for run functions on each goal in domain==================================================================
def extract_parameters_for_process_goal(goal , domain_name):
    match domain_name:
        
        case "blocks-world":
            goal_match = pattern_matcher(goal , domain_name)
            goal_word = create_word(goal_match)
            return goal_word
 
        
        case "easy-ipc-grid":
            goal_match = pattern_matcher(goal , domain_name)
            return goal_match

        case "sokoban":
            goal_match = pattern_matcher(goal , domain_name)
            goal_parameters_dictionary = dict_generator(goal_match)
            return goal_parameters_dictionary

        case "miconic":
            goal_match = pattern_matcher(goal , domain_name)
            entity_goal , priority_goal , entity_priority_goal = extract_priorities(goal_match)
            return entity_goal , priority_goal , entity_priority_goal

        case "intrusion-detection" | "rovers" | "zeno-travel" | "depots" | "driverlog" | "logistics" | "ferry" | "satellite" | "dwr":
            goal_match_pattern = pattern_matcher(goal , domain_name)
            goal_final_match = split_match_state(goal_match_pattern)
            goal_parameters_dictionary = extract_parameters_dynamic(goal_final_match)
            return goal_final_match , goal_parameters_dictionary
