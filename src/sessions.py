from src import sound, storage, timer, tasks

def pomodoro(state):
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
    state["total_time"] += focused_time
    state["total_sessions"] += 1
    state["longest_session"] = longest_check(focused_time, state["longest_session"])
    while True: #check after timer but before break
        task_completion = input('Did you complete any tasks? (y/n)\n')
        if task_completion.lower() == 'y':
            tasks.complete_task(state)
            break
        elif task_completion.lower() == 'n':
            print("Okay, continuing.\n")
            break
        else:
            print('Invalid input. Please enter y or n.\n')
    storage.save_data(state)
    print('Break time! Take a moment to reset.')
    timer.break_timer(break_minutes)
    sound.notification_sound()

def longest_check(focused_time, longest_session):
    if focused_time > longest_session:
        return focused_time
    return longest_session
