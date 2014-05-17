#True / False quiz created using simple 5 questions.
#To play the game visit: 
#http://www.codeskulptor.org/#user32_0nYZBj4nh2_2.py

import simplegui

width = 250
height = 200
color = "Navy"
current_question = 0
points = 0
answer = False

#List of questions
questions = ["","","","",""]
questions[0] = "Bear flag is official flag of state of California"
questions[1] = "Apple is a vegetable"
questions[2] = "China is a continent"
questions[3] = "Hawaii is awesome"
questions[4] = "Python is fun"

#Expected answers
answers = [True, False, False, True, True]

#Helper functions
def print_question():
    global current_question
    print "Question ", current_question + 1
    print questions[current_question]

def check_answer():
    global current_question, points, answer
    if answer == answers[current_question]:
        print "Correct :-) Good job!!!"
        points += 1
    else:
        print "Incorrect answer :-("
        current_question += 1
    if current_question == len(questions):
        print "Your score: ", points, "out of ", len(questions)
        print
        print
        print "Want to play again? Hit Restart"
    else:
        print_question()

#Event handlers

def true_button():
    global answer
    answer = True
    check_answer()

def false_button():
    global answer
    answer = False
    check_answer()

def new_game():
    global current_question, points
    current_question = 0
    points = 0
    print "Good luck!!!"
    print
    print_question()

#Frame
frame = simplegui.create_frame("Quiz", width, height)
frame.set_canvas_background(color)

# Register Event Handlers
frame.add_button("True", true_button, 50)
frame.add_button("False", false_button, 50)
frame.add_button("Restart", new_game, 50)

# Start Frame and Game
new_game()
frame.start()
