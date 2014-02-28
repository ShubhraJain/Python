# Reading the grades
# Grades are written as follows inside a file:
# Id Grade
# 001 75
# 002 38
# 003 45
# 



def read_grades(filename):
# Read the file and extract grades from each line and return a list containing all the grades

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
# Arrange the grades from the above list into their particular range and 
# get the count of grades are in each range
    

# Writing the histogram









