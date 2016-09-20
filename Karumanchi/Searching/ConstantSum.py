"""
Given an array A, find two numbers whose sum is equal to 'k'
"""

def find_numbers(input_list,k):
    """
    O(n^2) algorithm.
    :param input_list:
    :param k:
    :return:
    """
    temp_list = []
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if input_list[i]+input_list[j] == k :
                temp_list.append((input_list[i],input_list[j]))
    return temp_list

def _find_numbers(input_list):
    """

    :param input_list:
    :return:
    """
    return 0

def _find_numers_opt(input_list,k):
    """
    O(n) time
    :param input_list:
    :param k:
    :return:
    """

    table = {}

    for element in input_list:
        if element not in table:
            table[element] = element

    for element in input_list:
        if k-element in table:
            return table[k-element],element


if __name__=="__main__":
    test = [1,2,3,4,5,6,7]
    print(find_numbers(test,5))

    print(_find_numers_opt(test,5))