def main():
    print("please input a string:")
    user_string = input()
    str_for_checking = prepare_str_for_palindrome_checking(user_string)
    res = is_palindrome(str_for_checking)
    if(res == True):
        print("your sentence is a palindrome")
    else:
        print("your sentence is not a palindrome")

def prepare_str_for_palindrome_checking(s):
    only_letters_str = keep_only_letters(s)
    return only_letters_str.lower()

def keep_only_letters(s):
    res_str = ''
    for char in s:
        if(char.isalpha() == True):
            res_str = res_str + char
    return res_str

def is_palindrome(s):
    rev_s = reverse_str(s)
    if(s == rev_s):
        return True
    else:
        return False


def reverse_str(s):
    res_str = ''
    for char in s:
        res_str = char + res_str
    return res_str
main()