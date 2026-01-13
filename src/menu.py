from src import tasks, sessions

def menu(state):
    while True:
        print('=== Menu ===')

        print('1. Start pomodoro timer')
        print('2. Tasks')
        print('3. Stats')
        print('4. Achievements')
        print('5. Quit')

        choice = get_int('Please choose an option:\n')
        if choice == 1:
            sessions.pomodoro(state)
        elif choice == 2:
            tasks_menu(state)
        # elif choice == 3:
        #     stats_menu()
        # elif choice == 4:
        #     achievements_menu()
        elif choice == 5:
            print("Thank you for using my timer, can't wait to see you again!")
            break

def tasks_menu(state): #second layer of menu accessed via original menu
    while True:
        print('1. View tasks')
        print('2. Add task')
        print('3. Remove task')
        print('4. Show completed tasks')
        print('5. Back to main menu')

        choice = get_int('Please choose an option:\n')
        if choice == 1:
            tasks.show_task(state)
        elif choice == 2:
            tasks.add_task(state)
        elif choice == 3:
            tasks.remove_task(state)
        elif choice == 4:
            if not state["completed_tasks"]:
                print("No completed tasks yet. \n")
            else: 
                for i, t in enumerate(state["completed_tasks"]):
                    print(f'{i+1}. {t}')
        elif choice == 5:
            break

# def stats_menu():
#     while True:

# def achievements_menu():
#     while True:

def get_int(prompt): #input validation for menu number options
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print('Invalid input, please try again.\n')