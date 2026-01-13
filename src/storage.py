from pathlib import Path
import json

root = Path(__file__).parent.parent
save_file = root / "data" / "save_data.json"

default_data = {
    "tasks" : [],
    "completed_tasks" : [],
    "achievements" : [],
    "total_time" : 0,
    "streak" : 0,
    "longest_session" : 0,
    "total_sessions" : 0,
    "focused_days" : 0,
    "last_focus_date" : None
}

def load_data(): #using try/except, function will continue even if no input file is found
    try:
        with open(save_file, "r") as f:
            data = json.load(f)
            return {**default_data, **data}
    except (FileNotFoundError, json.JSONDecodeError):
        print("Save file missing, creating new file.\n")
        return default_data.copy()

def save_data(data): #output file will be created when saving, and can be used as input later
    save_file.parent.mkdir(exist_ok=True)
    with open(save_file, "w") as f:
        json.dump(data, f, indent=4)