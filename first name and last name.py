print('please enter your name. separate first name and last name by space: ')
full_name = input()

space_ind = full_name.find(' ')
first_name = full_name[ : space_ind]
last_name = full_name[space_ind+1 : ]
initials = first_name[0] + last_name[0]

print('firstname', first_name)
print('lastname', last_name)
print('initials', initials)