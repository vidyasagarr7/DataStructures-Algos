
"""
Print all permutations with repetition of characters

Given a string of length n, print all permutation of the given string. Repetition of characters is allowed.
Print these permutations in lexicographically sorted order

Examples:

Input: AB
Ouput: All permutations of AB with repetition are:
      AA
      AB
      BA
      BB

Input: ABC
Output: All permutations of ABC with repetition are:
     AAA
     AAB
     AAC
     ABA
     ...
     ...
     ...
     CCB
     CCC

"""

def permutations(string, temp_str, left, right, index):

    for i in range(left,right+1):
        temp_str[index] = string[i]
        if index == right:
            print(''.join(temp_str))
            return ''.join(temp_str)
        else :
            permutations(string, temp_str, left, right, index+1)

def print_permutations(string):
    out_string = [0]*len(string)
    permutations(list(string), out_string, 0, len(string)-1, 0)

if __name__=='__main__':
    string = 'ABC'
    print(print_permutations(string))















