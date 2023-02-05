print('please enter the number of students in the class:')
number_of_students = int(input())

print('please enter the grades of the students in seperate lines:')
grades_sum = 0

for i in range(number_of_students):
    curr_grade = int(input())
    grades_sum += curr_grade

average = grades_sum / number_of_students
print('the class average is', average)