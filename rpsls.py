#To play this game visit: http://www.codeskulptor.org/#user29_ldOvao7Hqb_1.py

#Game rule:
#Scissors cut paper
#Paper covers rock
#Rock crushes lizard
#Lizard poisons Spock
#Spock smashes scissors
#Scissors decapitate lizard
#Lizard eats paper
#Paper disproves Spock
#Spock vaporizes rock
#And as always, rock crushes scissors

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#This is how the player will say his name
def name_to_number(name):
    if (name == "rock"):
	return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print 'Invalid entry'

#This is how the computer number gets converted into 
#corresponding number as above
def number_to_name(number):												     
    if (number == 0):       
	return 'rock'
    if (number == 1):													  
        return 'Spock'
    if (number == 2):
	return 'paper'
    if (number == 3):
	return 'lizard'
    if (number == 4):
	return 'scissors'
    else:
        print 'Invalid entry'
    
def rpsls(player_choice):
#Prints player choice
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice)
#Computer's choice
    computer_number = random.randrange(0,5)
    print 'Computer chooses ' + number_to_name(computer_number)
                        
    diff = (computer_number - player_number) % 5

#Gets the winner according to the game rule
#Game rule is given at the top
    if (diff == 1 or diff == 2):
        print 'Computer wins!'
    elif (diff == 3 or diff == 4):
        print 'Player wins!'
    else:
        print 'Player and computer tie!'								      
    print '\n'

#Playing the game
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

