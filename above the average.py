def read_list():
    seen_done = False
    res_list = []
    while(seen_done == False):
        curr_input = input()
        if(curr_input == 'done'):
            seen_done = True
        else:
            curr = int(curr_input)
            res_list.append(curr)
    return res_list

def calc_average(lst):
    elems_sum = 0
    for elem in lst:
        elems_sum += elem
    average = elems_sum / len(lst)
    return average


def filter_above_value(lst, val):
    res_list = []
    for elem in lst:
        if(elem > val):
            res_list.append(elem)
    return res_list

def main():
    print('enter grades in seperate lines. to end type "done": ')
    grades_list = read_list()
    average = calc_average(grades_list)
    print('the class average is', average)
    above_avg_list = filter_above_value(grades_list, average)
    print(above_avg_list)

main()