# countdown-timer cli

import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')

        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown(int(input("Enter the number of seconds to countdown: ")))   
