
def find_min_max(input_list):
    """
    Algorithm to find minimum and maximum in an unsorted list
    :param input_list:
    :return:
    """
    minimum = maximum = input_list[0]

    for i in range(1,len(input_list)):
        if minimum > input_list[i]:
            minimum = input_list[i]
        if maximum < input_list[i]:
            maximum = input_list[i]
    return minimum,maximum

def find_min_max_opt(input_list):
    minimum = input_list[0]
    maximum = input_list[0]
    for i in range(1,len(input_list),2):
        first = input_list[i]
        second = input_list[i+1]
        if first < second :
            if first < minimum :
                minimum = first
            if second > maximum:
                maximum = second
        else :
            if second < minimum:
                minimum = second
            if first > maximum :
                maximum = first

    return minimum,maximum


if __name__=="__main__":
    test_input = [23,45,565,62,62,72,75,46,25,62,77,22,24]
    print(find_min_max(test_input))
    print(find_min_max_opt(test_input))