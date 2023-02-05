print('please enter a line of text: ')
line = input()
space_count = 0
ind = 0

while(ind < len(line)):
    curr_char = line[ind]
    if(curr_char == ' '):
        space_count += 1
    ind += 1

num_of_words = space_count + 1
print('you typed', num_of_words, 'words')