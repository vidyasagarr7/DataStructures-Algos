

def linear_search_unsorted(input_array,element):
    """
    O(n) - linear search in unordered list
    :param input_array:
    :param key:
    :return:
    """
    for key in input_array:
        if element == key:
            return True
    return False

def search_ordered(input_list,element):
    """
    O(n) implementation for ordered list
    :param input_list:
    :return:
    """
    for key in input_list:
        if key == element :
            return True
        if key > element:
            return False
    return False



if __name__=="__main__":
    test = [32,54,56,87,23,7,6,89,34,26,8,14,74]

    print(linear_search_unsorted(test,5))
    print(linear_search_unsorted(test,7))

    test.sort()
    print(search_ordered(test,5))
    print(search_ordered(test,7))
