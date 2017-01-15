
from Karumanchi.Sorting import MergeSort
"""
print first k smallest elements in an array of n elements
"""

def k_smallest(input_list,k):
    """
    O(n^2) algorithm - print the first k smallest elements in an array
    :param input_list:
    :return:
    """
    for i in range(k):
        for j in range(i+1,len(input_list)):
            if input_list[j]<input_list[i]:
                input_list[i],input_list[j]=input_list[j],input_list[i]
        print(input_list[i])
    return
def _k_smallest(input_list,k):
    """
    O(n*logn) algorithm for finding the first k elemenst
    :param input_list:
    :return:
    """
    sorted_list  = MergeSort.merge_sort(input_list)
    for i in range(k):
        print(sorted_list[i])
    return

if __name__=="__main__":
    test = [9,8,7,6,5,4,3,2,1]
    print(k_smallest(test,1))
    test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(_k_smallest(test,2))