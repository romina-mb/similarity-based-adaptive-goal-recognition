import os
import re
import subprocess
import numpy as np
import pandas as pd
import statistics
import shutil
import json

from sklearn import linear_model

def func_precision(stringList, answer):
    goal_count = 0
    found = 0
    for result in stringList:
        if result == str(answer):
            found = 1
        goal_count += 1

    return found/(goal_count-1)

def func_recall(stringList, answer):
    found = 0
    for result in stringList:
        if result == str(answer):
            found = 1
            break
    return found

def func_accuracy(total, stringList, answer):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for result in stringList[0:-1]:
        if result == str(answer):
            tp += 1
        else:
            fp += 1

    fn = 1 - tp

    # total is the number of all goals
    tn = total - tp - fp - fn
    return (tp + tn)/(tn + tp + fp + fn)


def func_bacc(total, stringList, answer):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for result in stringList[0:-1]:
        if result == str(answer):
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


# return a list of each statistics for every testing case
def calculate_statistics(rows):
    length = rows.shape[0]

    precision = []
    recall = []
    accuracy = []
    b_accuracy = []

    for index, row in rows.iterrows():

        answer = row["Real_Goal"]
        results = row["Results"].split("/")
        all_candidates = row["Cost"].split("/")

        total = len(all_candidates)-1   # the last one is /

        p = func_precision(results, answer)
        r = func_recall(results, answer)
        a = func_accuracy(total, results, answer)
        bacc = func_bacc(total, results, answer)

        precision.append(p)
        recall.append(r)
        accuracy.append(a)
        b_accuracy.append(bacc)

    return precision, recall, accuracy, b_accuracy


# a data point of all goal candidates
def averagedDataPoint(rows, goals):
    length = rows.shape[0]

    precision = []
    recall = []
    accuracy = []
    b_accuracy = []

    std_bacc = []

    tmp_precision = []
    tmp_recall = []
    tmp_accuracy = []
    tmp_b_accuracy = []

    for index, row in rows.iterrows():

        answer = row["Real_Goal"]
        results = row["Results"].split("/")
        all_candidates = row["Cost"].split("/")

        total = len(all_candidates)-1   # the last one is /

        p = func_precision(results, answer)
        r = func_recall(results, answer)
        a = func_accuracy(total, results, answer)
        bacc = func_bacc(total, results, answer)

        tmp_precision.append(p)
        tmp_recall.append(r)
        tmp_accuracy.append(a)
        tmp_b_accuracy.append(bacc)

        if len(tmp_b_accuracy) == goals:
            precision.append(statistics.mean(tmp_precision))
            recall.append(statistics.mean(tmp_recall))
            accuracy.append(statistics.mean(tmp_accuracy))
            b_accuracy.append(statistics.mean(tmp_b_accuracy))
            std_bacc.append(statistics.stdev(tmp_b_accuracy))

            tmp_precision = []
            tmp_recall = []
            tmp_accuracy = []
            tmp_b_accuracy = []

    return precision, recall, accuracy, b_accuracy, std_bacc



def tailAverage(metric_list, num):
    length = len(metric_list)
    if length < num:
        return statistics.mean(metric_list[0 : length])
    else:
        return statistics.mean(metric_list[(length - num) : length])



#### find the last number appears in the string and sort by it
def sortByLastNumber(lst):
    tupleList = []
    for item in lst:
        if item == ".DS_Store":
            continue
        numbers = re.findall(r'[\d]+', item)
        tupleList.append((int(numbers[-1]), item))  # sort by the last number
    tupleList.sort()

    stringList = []
    for item in tupleList:
        stringList.append(item[1])
    return stringList

def reCreateDir(dirName):
    # Check whether the specified path exists or not
    isExist = os.path.exists(dirName)
    if isExist:
        # delete
        shutil.rmtree(dirName)

    os.makedirs(dirName)



############################# systems ################################
class GRsystem:
    def __init__(self, init_models, testing_data , category_name , new_goals_list, add_new_goal_option):
        self.init_models = init_models
        self.testing_data = testing_data
        self.category = category_name
        self.new_goals = new_goals_list
        self.add_new_goal_option = add_new_goal_option

        ## delete models and re-create it

        if os.path.exists('tmp_models'):
          shutil.rmtree('tmp_models')


        os.mkdir("tmp_models")
        self.models = "./tmp_models"

        source_folder = init_models
        destination_folder = self.models
        
        #Creating new goal Petri net names that should be deleted in the next step
        pnml_names = []
        for goal in self.new_goals:
            pnml_name = goal + ".xes.pnml"
            pnml_names.append(pnml_name)
            
        excluded_files = pnml_names
        
        self.new_goal_flag_list = {}
        for petrinet in excluded_files:
            self.new_goal_flag_list[petrinet] = True
            

        
        # List of files with .pnml extension in source folder
        # Petri net deletion of goals that were selected as new goals
        pnml_files = [file for file in os.listdir(source_folder) if file.endswith(".pnml") and file not in excluded_files]

        for file in pnml_files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.copy(source_path, destination_path)

        # ================================
        ## testing traces in drift (sort it)
        test_list = os.listdir(testing_data)
        self.test_list = sortByLastNumber(test_list)

        # fixed variables:
        self.recognizerJar = "./recognizer.jar"
        self.controllerJar = "./controller.jar"
        self.relearn_dir = "./Feedback/Add"
        self.num2relearn = 10
        self.numModels = self.countModels()

    def countModels(self):
        models = 0
        for item in os.listdir(self.models):
            if item[-5::] == ".pnml":
                models += 1
        return models


    def load_similar_goal_from_json_file(self, json_file, category):

        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            
            if item == category:
                goals_dict = {}
                for new_goal in data[item]:
                    similar_goals_list = []
                    similar_goals = data[item][new_goal].keys()
                    for similar_goal in similar_goals: 
                        similar_goals_list.append(similar_goal)
                        
                    goals_dict.update({new_goal : similar_goals_list})

        return goals_dict




    # Adding a new goal to the results
    import pandas as pd

    def add_new_goal_to_result(self , file_path , category):

        new_goal_dict = self.load_similar_goal_from_json_file("filtered_similarity.json", category)

        df = pd.read_csv(file_path, delimiter=",", dtype=str)

        column_name = "Results"

        if column_name not in df.columns:
            raise ValueError(f"column '{column_name}' not found!")

        df[column_name] = df[column_name].fillna("")

        last_valid_index = df[column_name].last_valid_index()

        if last_valid_index is not None:
            last_value = df.loc[last_valid_index, column_name]

            last_value_list = [num for num in last_value.split("/") if num.isdigit()]


            for new_goal, sim_goal in new_goal_dict.items():
                sim_goals_num = []
                for goal in sim_goal:
                    temp_goal = re.findall(r'\d+', goal)
                    sim_goals_num.append(temp_goal[0])
                    
                
                # Check for at least one match without adding multiple times
                if any(sim_goal_num in last_value_list for sim_goal_num in sim_goals_num) and self.new_goal_flag_list[f"{new_goal}.xes.pnml"] == True:
                    goal_num_match = re.search(r'\d+', new_goal)
                    new_goal_num = goal_num_match.group()
                    df.loc[last_valid_index, column_name] += new_goal_num + "/"
                    

        df.to_csv(file_path, index=False, sep=",", quoting=1)


    def recognizer(self, test_plan, real_goal, obs_percentage, output_stats, phi = 50, lamb=2.5, delta=2.1, threshold=0.8):
        command = [
        "java", "-cp", self.recognizerJar, "Recognizer", "-w", self.models, test_plan, real_goal,
        str(obs_percentage), str(phi), str(lamb), str(delta), str(threshold), output_stats
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        # print(result.stdout)
        # print(result.stderr)


    def controllerOpenLoop(self, option):
        os.system("java -jar %s %s %s %s" % (self.controllerJar, option, self.relearn_dir, self.num2relearn) )

    def controllerClosedLoopAve(self, option, current_acc, acc_threshold):
        os.system("java -jar %s %s %s %s %s" % (self.controllerJar, option, self.relearn_dir, current_acc, acc_threshold) )

    def checkIfRemine(self):
        flag = "no"
        # # re-mine and replace models (in tmp_models) -> self.models
        for file in os.listdir():   # this converted xes are in the root directory
            if os.path.isfile(file) and file.split(".")[1] == "xes":

                command_java = [
                    "java", "-cp", "miner.jar", "autoMiner", "-DFM", file, f"{file}.pnml", "0.8"
                ]
                subprocess.run(command_java, check=True)

                os.remove(file)

                destination_file = os.path.join(self.models, f"{file}.pnml")
                if os.path.exists(destination_file):
                    os.remove(destination_file)

                os.rename(f"{file}.pnml", destination_file)

                flag = "yes"
                
                ###Setting the flag to false for the new goal after relearning; meaning it is no longer a new goal.###
                if f"{file}.pnml" in self.new_goal_flag_list.keys() and self.new_goal_flag_list[f"{file}.pnml"] == True:
                    self.new_goal_flag_list[f"{file}.pnml"] = False

        return flag


    def run(self, obs_percentage, output_stats, option):
        #: options: "-no-relearn"
        # delete (prev) feedbacks and (prev) csv file

        if os.path.exists('./Feedback'):
          shutil.rmtree('./Feedback')

        os.system(f'rmdir /s /q "{output_stats}"')


        case_index = 0
        remine_count = 0

        # only for closed loop
        highest_n_acc = 0

        for test_plan in self.test_list:
            if test_plan == ".DS_Store":
                continue
            else:
                case_index += 1

            real_goal = re.findall(r'[\d]+', test_plan)[-2]
            test_plan = self.testing_data + "/" + test_plan
            print(test_plan)

            # recognize a single GR task
            self.recognizer(test_plan, real_goal, obs_percentage, output_stats)


            #True: New system; add new goal to the prediction list, False: Old system without new goal
            if self.add_new_goal_option == True:
                #If there is a new goal, add it
                if any(self.new_goal_flag_list[f"{new_goal}.xes.pnml"] == True for new_goal in self.new_goals):
                    self.add_new_goal_to_result(output_stats, self.category)
            
            else:
                pass



            # check if to relearn
            if option == "-no-relearn":
                pass

            if option == "-openloop": # -openloop: consists with jar file
                # need call the controller
                self.controllerOpenLoop(option)
                # remine model or not?
                relearnFlag = self.checkIfRemine()
                # add flag
                self.addRelearnFlag(output_stats, relearnFlag)

            if option == "-closedloop_ave_metric":
                ## prepare data to relearn: collect X recent cases for all goals
                self.recentNCases()
                # check statistics
                # usecols= ['Real_Goal','Time','Cost','Prob','Results','Relearn']
                data = pd.read_csv("./%s" % output_stats, usecols=[0,1,2,3,4])
                # p, r, a, bacc = calculate_statistics(data)
                p, r, a, bacc, std_bacc = averagedDataPoint(data, self.numModels)

                # calculate average bacc for every period and keep highest.
                if case_index >= self.num2relearn*self.numModels:
                    recent_n_acc = tailAverage(bacc, self.num2relearn)
                else:
                    recent_n_acc = 0

                if recent_n_acc > highest_n_acc:
                    highest_n_acc = recent_n_acc

                # if check to relearn:
                if case_index%(self.num2relearn*self.numModels) == 0 and len(bacc) >= self.num2relearn:

                    acc_threshold = highest_n_acc * 0.8
                    self.controllerClosedLoopAve(option, recent_n_acc, acc_threshold)

                # remine model or not?
                relearnFlag = self.checkIfRemine()
                # add flag
                self.addRelearnFlag(output_stats, relearnFlag)

            if option == "-closedloop-trend":
                self.recentNCases()
                data = pd.read_csv("./%s" % output_stats, usecols=[0,1,2,3,4])
                p, r, a, bacc, std_bacc = averagedDataPoint(data, self.numModels)

                # calculate average bacc for every period and keep highest.
                if case_index >= self.num2relearn*self.numModels:
                    recent_n_acc = tailAverage(bacc, self.num2relearn)
                else:
                    recent_n_acc = 0

                if recent_n_acc > highest_n_acc:
                    highest_n_acc = recent_n_acc

                # if check to relearn:
                if case_index%(self.num2relearn*self.numModels) == 0 and len(bacc) >= self.num2relearn:
                    # next n acc
                    pointID = len(bacc)
                    X = np.array(range(pointID-self.num2relearn+1, pointID+1, 1)).reshape(-1,1)
                    reg = linear_model.LinearRegression()
                    reg.fit(X, bacc[-self.num2relearn::])
                    next_n_acc = reg.predict( np.array(pointID+self.num2relearn).reshape(-1,1) )

                    # set threshold for relearn
                    # acc_threshold = tailAverage(bacc[-2*self.num2relearn : -self.num2relearn], self.num2relearn) * 0.8
                    acc_threshold = highest_n_acc * 0.8


                    print(next_n_acc)
                    print(acc_threshold)

                    self.controllerClosedLoopAve("-closedloop_ave_metric", next_n_acc[0], acc_threshold)

                # remine model or not?
                relearnFlag = self.checkIfRemine()
                # add flag
                self.addRelearnFlag(output_stats, relearnFlag)
                        


    def recentNCases(self):   # N = num2relearn
        for a_dir in os.listdir(self.relearn_dir):
            if a_dir == ".DS_Store":
                continue

            plans = os.listdir(self.relearn_dir + "/" + a_dir)
            plans = sortByLastNumber(plans)
            numOfPlans = len(plans)
            if numOfPlans > self.num2relearn:
                for i in range(1, numOfPlans):
                    former = self.relearn_dir + "/" + a_dir + "/sas_plan." + str(i)
                    latter = self.relearn_dir + "/" + a_dir + "/sas_plan." + str(i+1)

                    
                    shutil.move(latter, former) 



    #Function to add relearning flag column
    def addRelearnFlag(self, filename, relearnFlag):
        df = pd.read_csv(filename, delimiter=",", dtype=str, keep_default_na=False)
        new_column = "Relearn Flag"
        if new_column not in df.columns:
            df[new_column] = ""
        df.loc[df.index[-1], new_column] = relearnFlag
        df.to_csv(filename, index=False, sep=",", quoting=1, na_rep="")

        print("Relearn flag added successfully!")



if __name__ == "__main__":

    ################################ parameters ###################################
   
    source_folder = "../phase 1"
    filename = "filtered_similarity.json"    
    filename2 = "selected_new_goals.json"    
    
    source_path = os.path.join(source_folder, filename)

    destination_path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(source_path):
        print(f"File '{filename}' in folder '{source_folder}' not found!")
    else:
        shutil.copy2(source_path, destination_path)
        print(f"File '{filename}' copied successfully!")
         
    source_path = os.path.join(source_folder, filename2)

    destination_path = os.path.join(os.getcwd(), filename2)
    if not os.path.exists(source_path):
        print(f"File '{filename2}' in folder '{source_folder}' not found!")
    else:
        shutil.copy2(source_path, destination_path)
        print(f"File '{filename2}' copied successfully!")   
        
    # ------------------------------    
    test_dataset = "./experimental data instance/testing"  
    training_dataset = "./experimental data instance/training"  

    print("Test dataset exists:", os.path.exists(test_dataset))
    # print(test_dataset)

    obs_percentage = 0.5

    # system options: 1. "-no-relearn";
    #                 2. "-openloop";
    #                 3. "-closedloop_ave_metric";
    #                 4. "-closedloop-trend";
    

    option = "-openloop"
    
    #True: New system; add new goal to the prediction list, False: Old system without new goal
    add_new_goal_option = True

    output_dir = "../data results instance"
    
    with open(filename2, "r", encoding="utf-8") as file:
        all_new_goals_data = json.load(file)

    ###############################################################################

    reCreateDir(output_dir)
    # tests = os.listdir(test_dataset)
    tests = os.listdir(test_dataset)
    for domain in tests:
        if domain == ".DS_Store":
            continue
        for problem_name in os.listdir(os.path.join(test_dataset, domain)):
            if problem_name == ".DS_Store":
                continue

            init_models = os.path.join(training_dataset, domain, problem_name) # initial models
            testing_data = os.path.join(test_dataset, domain, problem_name)

            category = os.path.join(domain, problem_name).replace("\\", "/")
            
            
            new_goals_in_domain = all_new_goals_data[category]

            output_stats = os.path.join(output_dir, "%s_%s_per%s_%s.csv" % (problem_name, option, str(obs_percentage*100), add_new_goal_option ) )
            

            gr_system = GRsystem(init_models, testing_data, category, new_goals_in_domain , add_new_goal_option)
            gr_system.run(obs_percentage, output_stats, option)

