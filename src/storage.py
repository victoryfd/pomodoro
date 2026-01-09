from pathlib import Path
import json

root = Path(__file__).parent.parent
save_file = root / "data" / "save_data.json"

def load_data(): #using try/except, function will continue even if no input file is found
    global coins, tasks, completed_tasks, unlocks, current_pet
    try:
        with open(save_file, "r") as f:
            data = json.load(f)
            coins = data["coins"]
            tasks = data["tasks"]
            completed_tasks = data["completed_tasks"]
            unlocks = data["unlocks"]
            current_pet = data["current_pet"]
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_data(): #output file will be created when saving, and can be used as input later
    global coins, tasks, completed_tasks, unlocks, current_pet
    save_file.parent.mkdir(exist_ok=True)
    with open(save_file, "w") as f:
        data = {"coins" : coins ,"tasks" : tasks, "completed_tasks" : completed_tasks, "unlocks" : unlocks, "current_pet" : current_pet}
        json.dump(data, f, indent=4)