from Karumanchi.Sorting import MergeSort
from Karumanchi.Searching import ConstantSum

"""
find 3 numbers in array such that their sum is constant K

"""

### Brute force algo with O(n^3)


def _find_number(input_list,k):

    sorted_list = MergeSort.merge_sort(input_list)
    left = 0
    right = len(input_list)-1
    for i in range(len(sorted_list)-2):
        left = i+1
        right = len(input_list)-1
        while left < right :
            if input_list[left] + input_list[right] + input_list[i] ==k :
                return input_list[i],input_list[left],input_list[right]
            if input_list[left] + input_list[right] + input_list[i] > k :
                right -= 1
            elif input_list[left] + input_list[right] + input_list[i] < k :
                left += 1


def find_numbers(input_list,k):
    """
    O(n^2) algorithm
    :param input_list:
    :return:
    """
    sorted_list = MergeSort.merge_sort(input_list)
    a=b=0
    pairs_list =[]
    for i in range(len(input_list)):
        a,b = ConstantSum._find_numers_opt(input_list,k-input_list[i])
        pairs_list.append((a,b,input_list[i]))
    return pairs_list


if __name__=="__main__":
    test= [1,2,3,4,5,6,7]
    print(find_numbers(test,11))

    print(_find_number(test,11))
