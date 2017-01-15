

"""
Find duplicates in O(n) time and O(1) extra space

Given an array of n elements which contains elements from 0 to n-1, with any of these numbers
 appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.

This problem is an extended version of following problem.
"""

def find_duplicates(input_list):
    if not input_list :
        return
    else :

        for i in range(len(input_list)):
            if input_list[abs(input_list[i])] < 0 :
                print(abs(input_list[i]))
            else :
                input_list[abs(input_list[i])] = - input_list[abs(input_list[i])]

if __name__=='__main__':
    test = [1, 2, 3, 1, 3, 6, 6,5,5,7,8,9,4]
    find_duplicates(test)





