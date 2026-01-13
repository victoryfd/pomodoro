from src import timer
from src import sound
from src import storage

""" 
Pomodoro + to do list management + stats + achievements. CLI app
"""

#------------------------------------------------------------
#Global game variables
#------------------------------------------------------------
tasks = []
completed_tasks = []
achievements = []
total_time = 0
streak = 0
longest_session = 0
total_sessions = 0

def pomodoro():
    while True: #input validation loop before running the timer and break functions to ensure integer values are passed
        hours = input('Please input hours to focus: ')
        minutes = input('Please input minutes to focus: ')
        break_minutes = input('Please input how many minutes for break: ')

        try:
            hours = int(hours) 
            minutes = int(minutes)  
            break_minutes = int(break_minutes)
            #for avoiding negative time
            if hours < 0 or minutes < 0: 
                print('Please enter a non-negative number.')
                continue
            #avoid 0-minute pomodoros
            if hours == 0 and minutes == 0: 
                print('Please enter duration greater than 0.')
                continue
            #avoid 0 or negative minute breaks
            if break_minutes <= 0: 
                print('Please enter a break, you deserve it.')
                continue
            else:
                break
        except ValueError: 
            print('Invalid input, please enter number\n') 

    print('Starting session. Good luck!')

    focused_time = timer.countdown(hours, minutes)
    sound.notification_sound()
    print(f'Good job! You focused for {focused_time} minutes.')
    total_time += focused_time
    total_sessions += 1
    longest_session = longest_check(focused_time, longest_session)
    while True: #check after timer but before break
        task_completion = input('Did you complete any tasks? (y/n)\n')
        if task_completion.lower() == 'y':
            complete_task()
            break
        elif task_completion.lower() == 'n':
            print("Okay, continuing.\n")
            break
        else:
            print('Invalid input. Please enter y or n.\n')
    save_all()
    print('Break time! Take a moment to reset.')
    timer.break_timer(break_minutes)
    sound.notification_sound()

def longest_check(focused_time, longest_session):
    if focused_time > longest_session:
        return focused_time
    return longest_session

def add_task():
    task = input('Enter task to add: ')
    #avoid adding blank task
    while not task: 
        print('Please enter a task.')
        task = input('Enter task to add: ')
    tasks.append(task)
    save_all()
    print('Task added.')
    
def show_task():
    if not tasks:
        print("You have no tasks. \n")
        return
    for i, task in enumerate(tasks):
        print(f'{i+1}. {task}')

#input and index validation everytime I need a task selected in the menus
def choose_task(prompt):
    first_time = True #used for a different prompt the first time function runs
    if not tasks:
        print('You have no tasks.')
        return
    show_task()
    while True:
        if first_time: #uses first_time to show different prompt the first loop
            index = input(prompt)
            first_time = False
        else:
            index = input('Please enter a number. \n')
        try: 
            index = int(index) - 1 
            if index >= len(tasks) or index < 0: 
                print("That task number doesn't exist. Please try again. ")
                continue
            else:
                return index
        except ValueError:
            continue    

def remove_task(): #for removing a task without completing it in the menus
    choice = choose_task("Choose what task you'd like to remove\n")
    if choice is None:
        return
    tasks.pop(choice)
    save_all()
    print('Task removed.')

def complete_task(): #will only be used after a completed pomodoro cycle
    choice = choose_task('Which task did you complete?\n')
    if choice is None:
        return
    task = tasks.pop(choice)
    completed_tasks.append(task)
    save_all()
    print(f"Task completed: {task}\nGood job!\n")


def get_int(prompt): #input validation for menu number options
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print('Invalid input, please try again.\n')

def menu():
    while True:
        print('=== Menu ===')

        print('1. Start pomodoro timer')
        print('2. Tasks')
        print('3. Stats')
        print('4. Achievements')
        print('5. Quit')

        choice = get_int('Please choose an option:\n')
        if choice == 1:
            pomodoro()
        elif choice == 2:
            tasks_menu()
        # elif choice == 3:
        #     stats_menu()
        # elif choice == 4:
        #     achievements_menu()
        elif choice == 5:
            print("Thank you for using my timer, can't wait to see you again!")
            break

def tasks_menu(): #second layer of menu accessed via original menu
    while True:
        print('1. View tasks')
        print('2. Add task')
        print('3. Remove task')
        print('4. Show completed tasks')
        print('5. Back to main menu')

        choice = get_int('Please choose an option:\n')
        if choice == 1:
            show_task()
        elif choice == 2:
            add_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            if not completed_tasks:
                print("No completed tasks yet. \n")
            else: 
                for i, t in enumerate(completed_tasks):
                    print(f'{i+1}. {t}')
        elif choice == 5:
            break

# def stats_menu():
#     while True:

# def achievements_menu():
#     while True:

def save_all():
    storage.save_data({
        "tasks" : tasks,
        "completed_tasks" : completed_tasks,
        "achievements" : achievements,
        "total_time" : total_time,
        "streak" : streak,
        "longest_session" : longest_session,
        "total_sessions" : total_sessions
    })

state = storage.load_data()
tasks = state["tasks"]
completed_tasks = state["completed_tasks"]
achievements = state["achievements"]
total_time = state["total_time"]
streak = state["streak"]
longest_session = state["longest_session"]
total_sessions = state["total_sessions"]

menu()