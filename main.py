from src import storage, menu

""" 
Pomodoro + to do list management + stats + achievements. CLI app
"""
def main():
    state = storage.load_data()
    menu.menu(state)

main()