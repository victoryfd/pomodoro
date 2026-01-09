import time

def display_time(hours, minutes, seconds):
    if hours > 0: #if time is >1 hour, show hours, minutes and seconds
        print(f'{hours}:{minutes:02d}:{seconds:02d}', end="\r")
    else: #if time is < 1 hour, only show minutes and seconds
        print(f'{minutes:02d}:{seconds:02d}  ', end="\r")

#runs a timer and returns minutes that the user focused for
def countdown(hours, minutes): 
    total_time = hours * 3600 + minutes * 60
    ini_total_time = hours * 60 + minutes #for collecting score/coins at the end, 1 coin/minute 
    while total_time > 0:
        display_hours = total_time // 3600
        display_minutes = total_time % 3600 // 60
        display_seconds = total_time % 60
        display_time(display_hours, display_minutes, display_seconds)
        time.sleep(1) #makes timer wait 1 second so it doesn't loop through instantly
        total_time -= 1
    return ini_total_time

#break timer similar to countdown but doesn't need a return value as no coins earned
def break_timer(break_minutes): 
    total_time =  break_minutes * 60
    while total_time > 0:
        display_minutes = total_time // 60
        display_seconds = total_time % 60
        display_time(0, display_minutes, display_seconds)
        time.sleep(1)
        total_time -= 1