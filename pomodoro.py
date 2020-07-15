#This is a Python script that mimics the Pomodoro technique for focused studying.
import random
import time
import webbrowser
from datetime import datetime, timedelta

import pyautogui

musicvideos80s = {
        "Huey Lewis And The News - The Heart Of Rock & Roll":"https://www.youtube.com/watch?v=M7JVlpm0eRs","Huey Lewis And The News - I Want A New Drug":"https://www.youtube.com/watch?v=N6uEMOeDZsA",
        "Lionel Richie - All Night Long":"https://www.youtube.com/watch?v=nqAvFx3NxUM", "Queen - Don't Stop Me Now":"https://www.youtube.com/watch?v=HgzGwKwLmgM", 
        "Bee Gees - Night Fever":"https://www.youtube.com/watch?v=-ihs-vT9T3Q", "Rick Astley - Never Gonna Give You Up":"https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
        "Wham! - Wake Me Up Before You Go-Go":"https://www.youtube.com/watch?v=pIgZ7gMze7A", "Earth, Wind & Fire - September":"https://www.youtube.com/watch?v=Gs069dndIYk", 
        "Earth, Wind & Fire - Let's Groove":"https://www.youtube.com/watch?v=Lrle0x_DHBM", "Rick James - Give It To Me Baby":"https://www.youtube.com/watch?v=1dNIQVYGXbM", 
        "Phil Collins - Sussudio":"https://www.youtube.com/watch?v=r0qBaBb1Y-U", "Stevie Nicks - Stand Back":"https://www.youtube.com/watch?v=gwS9BIqbffU",
        "Fleetwood Mac - Dreams":"https://www.youtube.com/watch?v=Y3ywicffOj4", "Prince - Little Red Corvette":"https://www.youtube.com/watch?v=v0KpfrJE4zw", 
        "Rod Stewart - Young Turks":"https://www.youtube.com/watch?v=zQ41hqlV0Kk", "ZZ Top - Sharp Dressed Man":"https://www.youtube.com/watch?v=7wRHBLwpASw", 
        "Huey Lewis And The News - If This Is It":"https://www.youtube.com/watch?v=AaTQAaJWW54", "Huey Lewis & The News - Small World":"https://www.youtube.com/watch?v=pSmHy-02KfQ", 
        "We're Not Here for a Long Time (We're Here for a Good Time) - Huey Lewis":"https://www.youtube.com/watch?v=Evp3rE0IKlc", 
        "Huey Lewis And The News - Workin' For A Livin":"https://www.youtube.com/watch?v=lcIK3akktLU", "One of the Boys - Huey Lewis":"https://www.youtube.com/watch?v=cowkDqz-gM4"}

def pomodoro():
    print("\n\n") # printing new lines
    print("Let's start the Pomodoro studying technique!\n\nThis program is designed to assist the user to have 25 minutes of continous studying.\n")
    time.sleep(1)
    print("Here are the steps:\n\n1. Remove all distractions (phone, open internet tabs, irrelevant learning material).\n2. The program will start a timer for 25 mins. This is your time to learn!\n3. At the end of 25 mins, a popup will signal your 7-minute timed break.\n4. Your browser will open with a YouTube tab of a random 80s music video.\n5. When you're ready to resume the Porodomo, go to the Command Line to indicate you are ready to continue.\n")
    time.sleep(1)
    print("Enjoy the material your learning!\n\n")
    time.sleep(1)
    print("----------------------------------------------------------------------------------------------------")


    for i in range(1,4):
        temp_intial_time = datetime.now().strftime("%I:%M %p")
        raw_alarm_time = datetime.now() + timedelta(minutes=25)
        temp_alam_time = datetime.strftime(raw_alarm_time, "%I:%M %p")
        print("\n[STUDY TIME] ")
        print("Time now: %s\nBreak time: %s\n" % (temp_intial_time, temp_alam_time))
        print("Focus for 25 minutes without interuption.\n\nIf a distraction arises, write it down and then return to it during your break.\nThis is your %s run through the Pomodoro.\n" % i)
        # Sleeps for 25 minutes (1500 seconds)
        time.sleep(1500)

        # Saying congrats on a job well done.
        print("----------------------------------------------------------------------------------------------------\n\n")
        print("[BREAK TIME] Wow! You did it. Great job for focusing for 25 mins. Now for a 7 minute break.\n\n")
        print("----------------------------------------------------------------------------------------------------")
        
        # Post Studying Message box. Option to continue on or stop the program.
        post_messagebox = pyautogui.confirm(text="Hello,\n\nYou have completed 25 minutes on uninterupted studying. Well done.\nTime to take a 7 minute break.If you chose to continue on, select 'OK'. If not, select 'CANCEL' to end the program.\n\nCheers!\n", title='A Segment of Pomodoro Completed', buttons=['OK', 'CANCEL'])
        if post_messagebox == 'OK':
            global musicvideos80s
            webbrowser.open(random.choice(list(musicvideos80s.values())), new=1, autoraise=True)
            time.sleep(420)
            continue
        

        # Returning after break messagebox
        
        # Potentially create new function here!
        final_messagebox = pyautogui.confirm(text="Hello,\n\nYour break is all done.\nIf you wish to continue the Pomodoro, select 'OK'. If not, select 'CANCEL' to end the program.\n\nCheers!\n", title='Break Completed', buttons=['OK', 'CANCEL'])
        if final_messagebox == 'OK':
            continue
      
    else: 
        temp_intial_time = datetime.now().strftime("%I:%M %p")
        raw_alarm_time = datetime.now() + timedelta(minutes=25)
        temp_alam_time = datetime.strftime(raw_alarm_time, "%I:%M %p")
        print("\n[STUDY TIME] ")
        print("Time now: %s\nBreak time: %s\n" % (temp_intial_time, temp_alam_time))
        print("Focus for 25 minutes without interuption.\n\nIf a distraction arises, write it down and then return to it during your break.\nThis is your 4 th run through the Pomodoro.\n")
        # Sleeps for 25 minutes (1500 seconds)
        time.sleep(1500)

        # Saying congrats on a job well done.
        print("----------------------------------------------------------------------------------------------------\n\n")
        print("[BREAK TIME] Wow! You did it. Great job for focusing for 25 mins. Now for a 30 minute break.\n\n")
        print("----------------------------------------------------------------------------------------------------")

        # Post Studying Message box. Option to continue on or stop the program.
        last_messagebox = pyautogui.confirm(text="Hello,\n\nYou have completed 25 minutes on uninterupted studying. Well done.\nTime to take a 30 minute break.If you chose to continue on, select 'OK'. If not, select 'CANCEL' to end the program.\n\nCheers!\n", title='Last Segment of Pomodoro Completed', buttons=['OK', 'CANCEL'])
        if last_messagebox == 'OK':
            webbrowser.open(random.choice(list(musicvideos80s.values())), new=1, autoraise=True)
            
        # Starts timer for 30 mins (1800 seconds)
        time.sleep(1800)

        # Returning after break messagebox
        return_messagebox = pyautogui.confirm(text="Hello,\n\nYour break is all done.\nIf you wish to continue the Pomodoro, select 'OK'. If not, select 'CANCEL' to end the program.\n\nCheers!\n", title='Break Completed', buttons=['OK', 'CANCEL'])
        if return_messagebox == 'CANCEL':
            print('Finishing Pomodoro.')

if __name__ == "__main__":

    pomodoro()
