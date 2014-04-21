# To play the game, visit http://www.codeskulptor.org/#user30_uPD0qWQt8FT1flp_1.py
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in code
remaining_guess = 0
exact_number = -1

def range100():
    print "New game. Range is from 0 to 100"    
    global remaining_guess
    global exact_number
    remaining_guess = 7
    exact_number = random.randrange(0,100)

def range1000():
    print "New game. Range is from 0 to 1000"    
    global remaining_guess
    global exact_number
    remaining_guess = 10
    exact_number = random.randrange(0,1000)

def input_guess(number):
    global remaining_guess 
    if (remaining_guess < 1):
        print "Oops...You have lost the game!!!"
        return
    print "You entered: ", number
    number = int(number)   
    if (exact_number < 0):
        print "Please first select the range"
        return
    remaining_guess = remaining_guess -1 
    if number < exact_number:
        print "Higher!"
    elif exact_number < number:
        print "Lower!"
    else:
        print "Correct!"    
        return
    print "number of remaining guesses is ", remaining_guess

# create frame
f = simplegui.create_frame("Guess the number!", 250, 250)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 120)
f.add_button("Range is [0, 1000)", range1000, 120)
f.add_input("Enter the number", input_guess, 120)

# start frame
f.start()
