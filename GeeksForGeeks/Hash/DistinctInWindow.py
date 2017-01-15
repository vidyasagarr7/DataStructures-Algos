

"""
Count distinct elements in every window of size k
Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.

Example:

Input:  arr[] = {1, 2, 1, 3, 4, 2, 3};
            k = 4
Output:
3
4
4
3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

"""

def find_distinct(input_list,k):
    if not input_list :
        return
    else :
        if k == 1 :
            return input_list
        for i in range()