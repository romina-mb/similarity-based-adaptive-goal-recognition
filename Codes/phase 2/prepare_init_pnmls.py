
# =================for windows===========================

import os
import shutil

# Mine PNML from set of plans
############################ iterative ############################

def iter_convert(path):
    # check if it is set of plans:
    is_set_of_plans = False
    lstdir = os.listdir(path)
    for subPath in lstdir:
        if subPath[0] != "." and os.path.isfile(os.path.join(path, subPath)) and os.path.basename(subPath)[0:3] == "sas":
            is_set_of_plans = True
            break

    if is_set_of_plans:
        print("This is a set of plan: " + path)
        # convert plans to event logs:
        os.system(f"java -jar sas2xes.jar {path} {path}.xes")

        return path
    else:
        for subPath in lstdir:
            if subPath[0] != ".":
                iter_convert(os.path.join(path, subPath))


##############################################################
if __name__ == "__main__":

    training_data = "data/training_pn"

    iter_convert(training_data)

    shutil.move(training_data, "./miningPNMLS/")
    
    os.chdir("./miningPNMLS")
    os.system("java -jar mine_all_pnmls.jar -DFM ./training_pn/ 0.8")
    
    # Move back the directory
    shutil.move("./training_pn", f"../{training_data}")
    os.chdir("../")
