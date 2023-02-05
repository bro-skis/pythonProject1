import random

def list_of_dice_rolls(n):
    res_lst = []
    for count in range(n):
        curr_roll = random.randint(1, 6)
        res_lst.append(curr_roll)
    return res_lst

def main():
    print('please enter a positive integer:')
    num_input = int(input())
    dice_rolls_results = list_of_dice_rolls(num_input)
    print(dice_rolls_results)

main()