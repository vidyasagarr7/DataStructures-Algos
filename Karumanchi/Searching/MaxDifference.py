from Karumanchi.Sorting import MergeSort
"""
Given an array of integers, find the maximum difference between two elements
"""

def find_max_diff(input_list):
    """
    O(n^2) algorithm for finding the max
    :param input_list:
    :return:
    """
    max_diff= 0
    max_idx = 0
    min_idx = 0
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if max_diff < input_list[j]-input_list[i] :
                max_diff = input_list[j]-input_list[i]
                max_idx = j
                min_idx = i

    return input_list[max_idx],input_list[min_idx], max_diff

# REVISIT this 
# def _find_maxdiff(input_list):



if __name__=="__main__":

    test = [2,3,10,6,4,8,1]
    print(find_max_diff(test))