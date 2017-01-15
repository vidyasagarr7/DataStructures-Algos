

"""
Divide a string in N equal parts

Question:
Write a program to print N equal parts of a given string.
"""


def print_n_parts(input_str,n):
    if not input_str :
        return
    else  :
        _list = list(input_str)
        part = len(input_str)/n

        for i in range(len(input_str)):
            if i>0 and i%part == 0:
                print()
            print(input_str[i],end='')

if __name__=='__main__':
    string = 'a_simple_divide_string_quest'
    print_n_parts(string,4)