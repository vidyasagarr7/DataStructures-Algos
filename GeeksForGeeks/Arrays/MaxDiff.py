
"""

Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[] of integers, find out the difference between any two elements such that larger element appears
after the smaller number in arr[].

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
 If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)

"""


def find_maxdiff(input_list):
    if not input_list :
        return
    else :
        _min = input_list[0]
        max_diff = 0
        for i in range(1,len(input_list)):
            if input_list[i] < _min :
                _min = input_list[i]
            if max_diff < input_list[i] - _min :
                max_diff = input_list[i] - _min
        return max_diff

if __name__=='__main__':
    test  = [2,3,10,6,4,9,1]
    print(find_maxdiff(test))

    test2 = [7, 9, 5, 6, 3, 2]
    print(find_maxdiff(test2))