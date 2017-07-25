#Creates 35 quizzes with same questions but in random order, along with the answer key.

import random

#States and their capitals are stored in a dictionary with states being the keys and 
#their capitals as values.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files
for quizNum in range(3):
    #Create quiz and answer key files
    questionFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('quizanswers%s.txt' % (quizNum + 1), 'w')

    #Create header of the quiz
    questionFile.write('ID #:\n\nName:\n\n')
    questionFile.write('State Capitals Quiz (Form %s)' % (quizNum + 1))
    questionFile.write('\n\n')

    #shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    #make question for all 50 states
    for question in range(50):
        answer = capitals[states[question]]
        allanswers = list(capitals.values())
        del allanswers[allanswers.index(answer)]
        allanswers = random.sample(allanswers, 3)
        options = allanswers + [answer]
        random.shuffle(options)
        questionFile.write('%s. What is the capital of %s?\n' %(question + 1, states[question]))
        for i in range(4):
            questionFile.write('%s. %s\n' %('abcd'[i], options[i]))
        questionFile.write('\n')

        answerFile.write('%s. %s\n' %(question + 1, 'abcd'[options.index(answer)]))
    questionFile.close()
    answerFile.close()



