import sys
from Karumanchi.Sorting import MergeSort
"""
Given an array with both positive and negative elements, find two elements in array who sum is closest to zero
"""

def find_numbers(input_list):
    """
    O(n^2) solution
    :param input_list:
    :return:
    """

    num1 = 0
    num2 = 0
    min_sum = 10000
    for i in range(len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if abs(input_list[i]+input_list[j]) < min_sum:
                min_sum = abs(input_list[i]+input_list[j])
                num1 = input_list[i]
                num2=input_list[j]
    return num1,num2

def _find_numbers(input_list):
    """
    O(n*(log(n)) algorithm - Sort the input
    :param input_list:
    :return:
    """
    sorted_list = MergeSort.merge_sort(input_list)
    start_idx = 0
    end_idx = len(input_list)-1
    min_sum = sys.maxsize
    min_left = 0
    min_right = len(input_list)-1
    while start_idx<end_idx:
        current_sum = input_list[start_idx]+input_list[end_idx]
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            min_left = start_idx
            min_right = end_idx

        if current_sum<0:
            start_idx += 1
        if current_sum>0 :
            end_idx -=1
    return input_list[min_left],input_list[min_right]


if __name__=="__main__":
    test=[1,60,-10,70,-80,85]

    print(find_numbers(test))
    print(_find_numbers(test))