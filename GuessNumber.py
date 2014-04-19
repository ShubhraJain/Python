# helper function to start and restart the game
def new_game():
    print "New game. "


# define event handlers for control panel
def range100(number):
    global exact_number
    global remaining_guess
    if number > exact_number:
        print "Higher!"
        print "number of remaining guesses is ", (remaining_guess - 1)
    elif number < exact_number:
        print "Lower!"
        print "number of remaining guesses is ", (remaining_guess - 1)
    else:
        print "Correct!"    
        return
    
def range1000(number):
    global exact_number
    print exact_number
    if number > exact_number:
        print "Higher!"
    elif number < exact_number:
        print "Lower!"
    else:
        print "Correct!"
    
def input_guess(guess):
    print "Guess was ", guess
    range100(guess)
    
