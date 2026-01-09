from src import timer
from src import sound
from src import storage

""" 
Pomodoro + to do list management + coins + pet store. CLI app
"""

#------------------------------------------------------------
#Global game variables
#------------------------------------------------------------
tasks = []
completed_tasks = []
unlocks = []
coins = 0
current_pet = None

pets = {
    1: 'Cat',
    2: 'Chick',
    3: 'Robot',
    4: 'Rabbit'
}
#------------------------------------------------------------
#ASCII art
#------------------------------------------------------------
pet_ascii = {
    "Cat" : (" /\\_/\\\n"
             "( o.o )\n"
             " > ^ <\n"),
    "Chick" : ("  (•ө•)\n"
               " (  .  )\n"
               "  ^^ ^^\n"),
    "Robot" : (" [• •]\n"
               "(  _  )\n"
               "  |_|\n"),
    "Rabbit" : (" (\\__/)\n"
             "(='.'=)\n"
             "(\")_(\")\n" ),
}
#------------------------------------------------------------
 
def pomodoro():
    global coins
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
            print('invalid input, please enter number') 

    print('Starting session. Good luck!')
    #show pet if unlocked
    if current_pet: 
        print(pet_ascii[current_pet])

    earned_coins = timer.countdown(hours, minutes)
    sound.notification_sound()
    print(f'Good job! You earned {earned_coins} coins.')
    coins += earned_coins
    save_all()
    print('Break time! Take a moment to reset.')
    timer.break_timer(break_minutes)
    sound.notification_sound()
    while True: #after time and break,
        task_completion = input('Did you complete any tasks? (y/n)\n')
        if task_completion.lower() == 'y':
            complete_task()
            break
        elif task_completion.lower() == 'n':
            print("Okay, continuing.\n")
            break
        else:
            print('Invalid input. Please enter y or n.\n')

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

def complete_task(): #will only be used after a completed pomodoro cycle to reward coins
    global coins
    choice = choose_task('Which task did you complete?\n')
    if choice is None:
        return
    task = tasks.pop(choice)
    completed_tasks.append(task)
    coins += 5
    save_all()
    print(f"Task completed: {task}\nGood job! +5 coins\n")

    if current_pet:
        print('Your pet is proud of you!\n')
        print(pet_ascii[current_pet])

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
        print(f'You have {coins} coins')

        if current_pet:
            print(pet_ascii[current_pet])

        print('1. Start pomodoro timer')
        print('2. Tasks')
        print('3. Shop')
        print('4. Pets')
        print('5. Quit')

        choice = get_int('Please choose an option:\n')
        if choice == 1:
            pomodoro()
        elif choice == 2:
            tasks_menu()
        elif choice == 3:
            shop_menu()
        elif choice == 4:
            pets_menu()
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
            for i, t in enumerate(completed_tasks):
                print(f'{i+1}. {t}')
        elif choice == 5:
            break

def shop_menu(): #also accessed via original menu
    global coins, unlocks
    while True:
        print(f'You have {coins} coins')
        print('1. Cat - 100 coins')
        print('2. Chick - 100 coins')
        print('3. Robot - 100 coins')
        print('4. Rabbit - 100 coins')
        print('5. Back to main menu')
        choice = get_int("Please select the item you'd like to buy:\n")

        if choice in [1, 2, 3, 4]: #if a valid pet choice, will check if enough coins
            pet_name = pets[choice]
            if pet_name in unlocks: #prevents buyingn pet if already owned
                print('You already own this pet.\n')
            else:
                if coins >= 100:
                    coins -= 100
                    unlocks.append(pet_name)
                    print(f'You just bought {pet_name}!\n')
                    save_all()
                else:
                    print("You don't have enough coins.\n")
        elif choice == 5:
            break
        else:
            print('Invalid choice.\n')

def pets_menu(): 
    global current_pet
    if not unlocks:
        print('You have no pets yet.\n')
        return
    while True:
        if current_pet is not None:
            print(f'Current pet: \n{pet_ascii[current_pet]}')
        else:
            print("Current pet: None\n")

        for i, p in enumerate(unlocks): #prints every pet unlocked so far, along with the ASCII art
            print(f'{i+1}. {p}\n{pet_ascii[p]}\n')
        print(f'{len(unlocks)+1}. Back to main menu')

        choice = get_int('Which pet would you like to switch to?\n')

        if choice >= 1 and choice <= len(unlocks): #switch current pet if index is valid
            current_pet = unlocks[choice - 1]
            save_all()
        elif choice == len(unlocks) + 1:
            break
        else:
            print('Invalid choice.\n')

def save_all():
    storage.save_data({
        "coins" : coins,
        "tasks" : tasks,
        "completed_tasks" : completed_tasks,
        "unlocks" : unlocks,
        "current_pet" : current_pet
    })

state = storage.load_data()
coins = state["coins"]
tasks = state["tasks"]
completed_tasks = state["completed_tasks"]
unlocks = state["unlocks"]
current_pet = state["current_pet"]
menu()