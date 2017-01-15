from Karumanchi.Sorting import MergeSort
"""
An element is a majority element if it appears more than n/2 times.
"""

def find_majority(input_list):
    """
    O(n^2) algorithm
    :param input_list:
    :return:
    """
    count =0
    max_count = 0
    max_element_idx = 0
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if input_list[i]==input_list[j]:
                count +=1
            else:
                count = 1
            if max_count < count:
                max_count = count
                max_element_idx = i
    if max_count > len(input_list)//2:
        return input_list[max_element_idx]
    else :
        return -1

def _find_majority(input_list):
    """
    O(n*log(n)) algorithm
    :param input_list:
    :return:
    """
    sorted_list = MergeSort.merge_sort(input_list)
    max_count = 0
    count = 0
    maxcount_element_idx = 0
    for i in range(len(sorted_list)-1):
        if input_list[i]==input_list[i+1]:
            count+=1
        else:
            count = 1
        if max_count < count :
            max_count = count
            maxcount_element_idx = i
    if max_count > len(sorted_list)//2:
        return sorted_list[maxcount_element_idx]
    else :
        return -1


def __find_majority_opt(input_list):
    """
    O(n) time  algorithm - Assuming that only one element in the array is repeating and it repeats more than n/2 times.
    :param input_list:
    :return:
    """
    count = 0
    element = input_list[0]
    for i in range(len(input_list)):
        if count == 0 :
            element = input_list[i]
            count =1
        elif element == input_list[i]:
            count +=1
        else :
            count -=1
    return element

if __name__ =="__main__":
    test = [1,2,2,2,3,4,5,5,5,2,2,2,2,2]
    print(find_majority(test))

    print(_find_majority(test))
    print(__find_majority_opt(test))