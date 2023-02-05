grade = int(input('please enter a grade: '))

if(89 < grade <= 100):
     print(grade, 'is A')
elif(79 < grade <= 89):
     print(grade, 'is B')
elif(69 < grade <= 79):
     print(grade, 'is C')
elif(59 < grade <= 69):
     print(grade, 'is D')
elif(-1 < grade <= 59):
     print(grade, 'is F')
else:
     print(grade, 'is invalid')