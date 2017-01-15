"""
Write a program to print all permutations of a given string

A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of
an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.
Source: Mathword(http://mathworld.wolfram.com/Permutation.html)

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB

"""

def print_permutations(string,left,right):
    if left==right :
         print(''.join(string))
    else :

        for i in range(left,right) :
            string[left],string[i] = string[i],string[left]
            print_permutations(string,left+1,right)
            string[left],string[i] = string[i],string[left]

if __name__=='__main__':
    input_string = 'ABC'
    print(print_permutations(list(input_string),0,len(input_string)))