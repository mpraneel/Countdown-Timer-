# @author Praneel Magapu
# Basic countdown timer in Python3

# importing the time module
import time

# define countdown function
def countdown(val):

    while val: 
        mins, secs = divmod(val, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        val -= 1
      
    print('Beep Beep!') 

# take the input of time
val = input('Countdown from: ')
  
# function call 
countdown(int(val)) 