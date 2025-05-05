
def compute_grade(points):
  if points >= 70:
    return 'A'
  elif points >=50:
    return 'B'
  elif points >=30:
    return 'C'
  else:
    return 'F'
  
#Call the function to convert 39 points to a letter grade
compute_grade(39)

def report_message(name, points):
  return name + " scored " + str(points) + "/100 points in Chemistry and got the letter " + compute_grade(points)

#Call the function for you friend Zach
report_message("Zach", 51)

#Creat a text file for Zach's report card and write the message inside
result_file = open("zach_report.txt", 'w')
result_file.write(report_message("Zach", 51))
result_file.close()

#Check if there is already a report card for Sophie and print a message in case there is
try:
  result_file = open("sophie_report.txt", 'r')
  print('There is an existing report card for Sophie')
#If there is none, create one and write the message inside
except:
  result_file = open("sophie_report.txt", 'w')
  result_file.write(report_message("Sophie", 78))

result_file.close()



def student_grade(name, points):
  #return name:grade
  try:
    return (name + ':' + compute_grade(points))
  #or return a message if the student was missing
  except:
    return (name + ' was missing during the exam.')
  

#Run the list of all students and their points
student_list = [('Oğuzhan', 100), ('Zach', 51), ('Sophie', 78), ('Fred', 29), ('Belina','missing'), ('Markus','missing')]

for name, points in student_list:
  grade = student_grade(name, points)
  #print the message returned by student_grade
  print(grade)

#Create the grades.txt file
grades_file = open("grades.txt", 'w')

for name, points in student_list:
  grade = student_grade(name, points)
  #Write the message returned by student_grade into the file
  grades_file.write(grade + '\n')

#Close the file
grades_file.close()