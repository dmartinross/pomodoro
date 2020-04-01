#This is a Python script that mimics the Pomodoro technique for focused studying.
from datetime import datetime
from datetime import timedelta
import time
import webbrowser
import random
import ctypes


def pomodoro():
    intial_time = datetime.now().strftime("%I:%M %p")
    raw_alarm_time = datetime.now() + timedelta(minutes=25)
    alarm_time = datetime.strftime(raw_alarm_time, "%I:%M %p")
    print("Heads up. It is %s right now.\n\n" % intial_time)
    print("This program is designed to assist the user using the Pomodoro studying technique of 25 mins of continous studying.\n")
    print("There will be a popup at %s to notify you of your break.\nOnce the popup is closed, then there will be a surprise popup of a YouTube video." % alarm_time)
    print("A random 80s music video will start. Until then, enjoy the material!\n\n")


    for i in range(1,4):
        print("Focus for 25 minutes without interuption.\n\nIf a distraction arises, write it down and then return to it during your break.\nThis is your %s run through the Pomodoro.\n" % i)
        # Sleeps for 25 minutes (1500 seconds)
        time.sleep(5)

        # Saying congrats on a job well done.
        print("Wow! You did it. Great job for focusing for 25 mins. Now for a 7 minute break.\n\n\n\n")

        # Message box
      
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Hello,\n\nYou have completed 25 minutes on uninterupted studying. Well done.\nTime to take a 7 minute break.\n\nCheers!\n', 'A Segment of Pomodoro Completed', 0)
       
        # Opens random 80s music video from dictionary
        musicvideos80s_list = {
        "Huey Lewis And The News - The Heart Of Rock & Roll":"https://www.youtube.com/watch?v=M7JVlpm0eRs","Huey Lewis And The News - I Want A New Drug":"https://www.youtube.com/watch?v=N6uEMOeDZsA",
        "Lionel Richie - All Night Long":"https://www.youtube.com/watch?v=nqAvFx3NxUM", "Queen - Don't Stop Me Now":"https://www.youtube.com/watch?v=HgzGwKwLmgM", 
        "Bee Gees - Night Fever":"https://www.youtube.com/watch?v=-ihs-vT9T3Q", "Rick Astley - Never Gonna Give You Up":"https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
        "Wham! - Wake Me Up Before You Go-Go":"https://www.youtube.com/watch?v=pIgZ7gMze7A", "Earth, Wind & Fire - September":"https://www.youtube.com/watch?v=Gs069dndIYk", 
        "Earth, Wind & Fire - Let's Groove":"https://www.youtube.com/watch?v=Lrle0x_DHBM", "Rick James - Give It To Me Baby":"https://www.youtube.com/watch?v=1dNIQVYGXbM", 
        "Phil Collins - Sussudio":"https://www.youtube.com/watch?v=r0qBaBb1Y-U", "Stevie Nicks - Stand Back":"https://www.youtube.com/watch?v=gwS9BIqbffU",
        "Fleetwood Mac - Dreams":"https://www.youtube.com/watch?v=Y3ywicffOj4", "Prince - Little Red Corvette":"https://www.youtube.com/watch?v=v0KpfrJE4zw", 
        "Rod Stewart - Young Turks":"https://www.youtube.com/watch?v=zQ41hqlV0Kk", "ZZ Top - Sharp Dressed Man":"https://www.youtube.com/watch?v=7wRHBLwpASw", 
        "Madness - Our House":"https://www.youtube.com/watch?v=oXA6CLTDekw"}
        webbrowser.open(random.choice(list(musicvideos80s_list.values())), new=1, autoraise=True)
        
        # Starts timer for 7 mins (420 seconds)
        time.sleep(420)
      
    else: 
        print("Focus for 25 minutes without interuption.\n\nIf a distraction arises, write it down and then return to it during your break.\nSince this is the 4th Pomodoro, your next break will be 30 minutes!")
        
        # Sleeps for 25 minutes (1500 seconds)
        time.sleep(1500)

        # Saying congrats on a job well done. 
        print("Wow! You did it. Great job for focusing for the last 25 mins. Now for a 30 minute break and then return to start the Porodoro again.\n\n\n\n")

        # Message box
      
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Hello,\n\nYou have completed 25 minutes on uninterupted studying. Well done.\nTime to take a 30 minute break before coming back.\n\nCheers!\n', 'Last Segment of Pomodoro Completed', 0)
       
        # Opens random 80s music video from dictionary
        musicvideos80s_list = {
        "Huey Lewis And The News - The Heart Of Rock & Roll":"https://www.youtube.com/watch?v=M7JVlpm0eRs","Huey Lewis And The News - I Want A New Drug":"https://www.youtube.com/watch?v=N6uEMOeDZsA",
        "Lionel Richie - All Night Long":"https://www.youtube.com/watch?v=nqAvFx3NxUM", "Queen - Don't Stop Me Now":"https://www.youtube.com/watch?v=HgzGwKwLmgM", 
        "Bee Gees - Night Fever":"https://www.youtube.com/watch?v=-ihs-vT9T3Q", "Rick Astley - Never Gonna Give You Up":"https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
        "Wham! - Wake Me Up Before You Go-Go":"https://www.youtube.com/watch?v=pIgZ7gMze7A", "Earth, Wind & Fire - September":"https://www.youtube.com/watch?v=Gs069dndIYk", 
        "Earth, Wind & Fire - Let's Groove":"https://www.youtube.com/watch?v=Lrle0x_DHBM", "Rick James - Give It To Me Baby":"https://www.youtube.com/watch?v=1dNIQVYGXbM", 
        "Phil Collins - Sussudio":"https://www.youtube.com/watch?v=r0qBaBb1Y-U", "Stevie Nicks - Stand Back":"https://www.youtube.com/watch?v=gwS9BIqbffU",
        "Fleetwood Mac - Dreams":"https://www.youtube.com/watch?v=Y3ywicffOj4", "Prince - Little Red Corvette":"https://www.youtube.com/watch?v=v0KpfrJE4zw", 
        "Rod Stewart - Young Turks":"https://www.youtube.com/watch?v=zQ41hqlV0Kk", "ZZ Top - Sharp Dressed Man":"https://www.youtube.com/watch?v=7wRHBLwpASw", 
        "Madness - Our House":"https://www.youtube.com/watch?v=oXA6CLTDekw"}
        webbrowser.open(random.choice(list(musicvideos80s_list.values())), new=1, autoraise=True)
        
        # Starts timer for 30 mins (1800 seconds)
        time.sleep(1800)
       

if __name__ == "__main__":

    pomodoro()
