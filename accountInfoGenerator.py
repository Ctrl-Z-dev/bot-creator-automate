import string 
import random
import pyautogui as gui
import time
import sys
import random

# Generating name functions 
# You can create different surnames to increase the variety of usernames.
def generatingName():
    firstName = [name_list.txt]

    surName =[name_list.txt]
    return ''.join(random.choice(name_list.txt) + ' '  + random.choice(name_list.txt))    


# Generating a username
def username(size = 6, chars  = string.ascii_lowercase + random.choice(['.', '_'])):
    return ''.join(random.choice(chars) for _ in range(size))

