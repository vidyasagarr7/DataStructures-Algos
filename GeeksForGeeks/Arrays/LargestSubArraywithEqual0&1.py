
"""
Largest subarray with equal number of 0s and 1s

Given an array containing only 0s and 1s, find the largest subarray which contain equal no of 0s and 1s.
 Expected time complexity is O(n).
"""

def lsa(input_list):
    if not input_list :
        return
    else :
        _sum = input_list[0]
        sum_arr = [0]*len(input_list)
        for i in range(1,len(input_list)):
            _sum