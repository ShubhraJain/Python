"""
Grades are written inside a file as follows
Id Grade
001 75
002 38
003 45
"""

def read_grades(filename):
    """
    Read the file and extract grades from each line and
    return a list containing all the grades.
    """
    f = open(filename, 'r')
    grades = []
    lines = f.readline()
    while (lines != ''):
          line = lines
          lines = f.readline()
          for i in range(len(line)):
              if (line[i] == ' '):
                 grades.append(int(line[i+1:]))
    f.close()
    return grades

print(read_grades('grades_file.txt'))       

def range_grades(grades):
    """
    Arrange the grades from the above list into their particular range and 
    get the count of grades that are in each range
    >>> range_grades([75, 38, 45]) 
    [0,0,0,1,1,0,0,1,0,0,0]
    """
    count_grades = [0] * 11
    for i in range(len(grades)):
        j = grades[i] // 10   
        count_grades[j] += 1
    return count_grades

print(range_grades(read_grades('grades_file.txt')))
        
def range_histogram(list_of_grades): 
    """ 
    Prints the histogram of the grades 
    >>> range_histogram([0,0,0,1,1,0,0,1,0,0,0])
    0 - 9: 
    10 - 19: 
    20 - 29: 
    30 - 39: *
    40 - 49: *
    50 - 59: 
    60 - 69: 
    70 - 79: *
    80 - 89: 
    90 - 99: 
    100:  
    """
    for i in range(len(list_of_grades) - 1):
        print ("%d - %d: %s" % (i * 10, i * 10 + 9, '*' * list_of_grades[i]))
    print ("%d: %s" % (100, '*' * list_of_grades[10]))

range_histogram(range_grades(read_grades('grades_file.txt')))

