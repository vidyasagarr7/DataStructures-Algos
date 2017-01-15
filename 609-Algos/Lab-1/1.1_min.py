
def find_min(input_list):
    """
    Find the minimum number in a unsorted list
    :param input_list: unsorted list
    :return: minimum number in the list
    """
    minimum = input_list[0]
    for i in range(1,len(input_list)):
        if input_list[i] < minimum :
            minimum = input_list[i]
    return minimum

if __name__=="__main__":
    test=[23,54,65,12,76,89,35,37,38]
    print(find_min(test))