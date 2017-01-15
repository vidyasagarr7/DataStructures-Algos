import sys

"""
Check if array elements are consecutive | Added Method 3

Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.

Examples:
a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers
from 1 to 5.

b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has
consecutive numbers from 78 to 83.

c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.

d) If the array is {7, 6, 5, 5, 3, 4}, then the function should return false because 5 and 5 are not consecutive.

"""

def check_duplicates(input_list):
    return len(input_list) == len(set(input_list))

def check_consecutive(input_list):
    if not input_list :
        return
    else :
        _max = -sys.maxsize
        _min = sys.maxsize

        for num in input_list :
            if num < _min :
                _min = num
            if num > _max :
                _max = num
        if _max - _min == len(input_list)-1 and check_duplicates(input_list):
            return True
        return False

if __name__=='__main__':
    test = [5, 2, 3, 1, 4]
    print(check_consecutive(test))

    test1 = [83, 78, 80, 81, 79, 82]
    print(check_consecutive(test1))

    test2 = [34, 23, 52, 12, 3]
    print(check_consecutive(test2))

    test3 = [7, 6, 5, 5, 3, 4]
    print(check_consecutive(test3))
