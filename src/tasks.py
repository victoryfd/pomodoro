from src import storage

def add_task(state):
    task = input('Enter task to add: ')
    #avoid adding blank task
    while not task: 
        print('Please enter a task.')
        task = input('Enter task to add: ')
    state["tasks"].append(task)
    storage.save_data(state)
    print('Task added.')
    
def show_task(state):
    if not state["tasks"]:
        print("You have no tasks. \n")
        return
    for i, task in enumerate(state["tasks"]):
        print(f'{i+1}. {task}')

#input and index validation everytime I need a task selected in the menus
def choose_task(state, prompt):
    first_time = True #used for a different prompt the first time function runs
    if not state["tasks"]:
        print('You have no tasks.')
        return
    show_task(state)
    while True:
        if first_time: #uses first_time to show different prompt the first loop
            index = input(prompt)
            first_time = False
        else:
            index = input('Please enter a number. \n')
        try: 
            index = int(index) - 1 
            if index >= len(state["tasks"]) or index < 0: 
                print("That task number doesn't exist. Please try again. ")
                continue
            else:
                return index
        except ValueError:
            continue    

def remove_task(state): #for removing a task without completing it in the menus
    choice = choose_task(state, "Choose what task you'd like to remove\n")
    if choice is None:
        return
    state["tasks"].pop(choice)
    storage.save_data(state)
    print('Task removed.')

def complete_task(state): #will only be used after a completed pomodoro cycle
    choice = choose_task(state, 'Which task did you complete?\n')
    if choice is None:
        return
    task = state["tasks"].pop(choice)
    state["completed_tasks"].append(task)
    print(f"Task completed: {task}\nGood job!\n")