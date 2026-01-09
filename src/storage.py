import json

def load_data(): #using try/except, function will continue even if no input file is found
    global coins, tasks, completed_tasks, unlocks, current_pet
    try:
        with open("save_data.json", "r") as f:
            data = json.load(f)
            coins = data["coins"]
            tasks = data["tasks"]
            completed_tasks = data["completed_tasks"]
            unlocks = data["unlocks"]
            current_pet = data["current_pet"]
    except FileNotFoundError:
        pass

def save_data(): #output file will be created when saving, and can be used as input later
    global coins, tasks, completed_tasks, unlocks, current_pet
    with open("save_data.json", "w") as f:
        data = {"coins" : coins ,"tasks" : tasks, "completed_tasks" : completed_tasks, "unlocks" : unlocks, "current_pet" : current_pet}
        json.dump(data, f, indent=4)