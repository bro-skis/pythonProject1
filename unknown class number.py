print("please enter the grades of students in seperate lines. To end the input type 'done': ")

grade_sum = 0
student_count = 0
seen_done = False
while(seen_done == False):
    curr_input = input()
    if(curr_input == 'done'):
        seen_done = True
    else:
        curr_grade = int(curr_input)
        grade_sum += curr_grade
        student_count += 1

average = grade_sum / student_count
print('the student average is', average)