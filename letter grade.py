print('please enter a grade: ')
grade = int(input())

if(89 < grade <= 100):
    print(grade, 'is A')
else:
    if(79 < grade <= 89):
        print(grade, 'is B')
    else:
        if(69 < grade <= 79):
             print(grade, 'is C')
        else:
            if(59 < grade <= 69):

                     print(grade, 'is D')
            else:
                if (-1 < grade <= 59):
                  print(grade, 'is F')
                else:
                    print(grade, 'is invalid')