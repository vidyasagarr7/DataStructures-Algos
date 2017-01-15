
def binary_search(input_list,key):
    """
    Binary search algorithm for finding if an element exists in a sorted list.
    Time Complexity : O(ln(n))
    :param input_list: sorted list of numbers
    :param key: key to be searched for
    :return:
    """

    if len(input_list) is 0:
        return False
    else :
        mid = len(input_list)//2
        if key == input_list[mid]:
            return True
        elif key < input_list[mid-1]:
            return binary_search(input_list[:mid-1],key)
        elif key > input_list[mid]:
            return binary_search(input_list[mid:],key)



if __name__=="__main__":
    test = [23,45,65,13,778,98,25,76,48,28,85,97]
    test.sort()
    print(binary_search(test,98))
    print(binary_search(test,12))