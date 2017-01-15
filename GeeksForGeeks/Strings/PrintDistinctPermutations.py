"""
Print all distinct permutations of a given string with duplicates
Given a string that may contain duplicates, write a function to print all permutations of given string
 such that no permutation is repeated in output.

Examples:

Input:  str[] = "AB"
Output: AB BA

Input:  str[] = "AA"
Output: AA

Input:  str[] = "ABC"
Output: ABC ACB BAC BCA CBA CAB

Input:  str[] = "ABA"
Output: ABA AAB BAA

Input:  str[] = "ABCA"
Output: AABC AACB ABAC ABCA ACBA ACAB BAAC BACA
        BCAA CABA CAAB CBAA

REVISIT
"""

def print_distinct_permutations(input_string,left,right):
    if left==right:
        print(''.join(input_string))
    else:
        #print('printing left {}'.format(left))
        for i in range(left,right):
            input_string[left],input_string[i] = input_string[i],input_string[left]
            print_distinct_permutations(input_string,left+1,right)
            input_string[left],input_string[i]=input_string[i],input_string[left]

if __name__=='__main__':
    string = list('ABCD')
    print_distinct_permutations(string,0,len(string))



