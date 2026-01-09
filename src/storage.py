from pathlib import Path
import json

root = Path(__file__).parent.parent
save_file = root / "data" / "save_data.json"

default_data = {
    "coins" : 0,
    "tasks" : [],
    "completed_tasks" : [],
    "unlocks" : [],
    "current_pet" : None
}

def load_data(): #using try/except, function will continue even if no input file is found
    try:
        with open(save_file, "r") as f:
            data = json.load(f)
            return {**default_data, **data}
    except (FileNotFoundError, json.JSONDecodeError):
        return default_data.copy()

def save_data(data): #output file will be created when saving, and can be used as input later
    save_file.parent.mkdir(exist_ok=True)
    with open(save_file, "w") as f:
        json.dump(data, f, indent=4)