
from Karumanchi.Sorting import MergeSort
from Karumanchi.Sorting import CountingSort

def check_duplicates(input_list):
    """
    O(n^2) algorithm to check for duplicates
    :param input_list:
    :return:
    """
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if input_list[i]==input_list[j]:
                return True

    return False

def check_duplicates_opt(input_list):
    """
    O(n*log(n)) algorithm - Sort the list

    :param input_list:
    :return:
    """
    sorted_list = MergeSort.merge_sort(input_list)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False

def check_duplicates_opt2(input_list):
    """
    considering the input elements in the range 0-(n-1) --> we can sort the array using counting sort in O(n) time and
    traverse in linear time
    :param input_list:
    :return:
    """
    sorted_list = CountingSort.counting_sort(input_list,10)
    for i in range(len(sorted_list)-1):
        if sorted_list[i]==sorted_list[i+1]:
            return True
    return False

def check_duplicates_negation(input_list):
    """
    Assumption : input list values range from 0-(n-1) and all numbers are positive.
    :param input_list:
    :return:
    """
    for i in range(len(input_list)):
        if input_list[input_list[i]]<0:
            return True
        else :
            input_list[input_list[i]] = -input_list[input_list[i]]
    return False



if __name__=="__main__":
    test = [1,2,3,4,6,7,8,9,4]

    print(check_duplicates(test))

    print(check_duplicates_opt(test))

    print(check_duplicates_opt2(test))

    print(check_duplicates_negation(test))
