

"""
Given an array A[] and a number x, check for pair in A[] with sum as x

Write a C program that, given an array A[] of n numbers and another number x,
determines whether or not there exist two elements in S whose sum is exactly x.



"""

def find_sum(input_arr, _sum):
    if not input_arr  :
        return False
    else :
        hash_table = {}
        for i in input_arr:
            # check if sum-number is already present in the array
            # function returns a single pair
            if _sum-i in hash_table :
                return i,hash_table[_sum-i]


            if i not in hash_table :
                hash_table[i] = i
        return 'sum not found'


if __name__=='__main__':
    input_arr = [1,2,3,4,5,6,7,8,9]
    print(find_sum(input_arr,14))