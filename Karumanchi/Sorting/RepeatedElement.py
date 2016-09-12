


def check_repeated(input_list):
    """
    O(n^2) solution
    :param input_list:
    :return:
    """
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if input_list[i]==input_list[j]:
                return True
    return False


def check_repeated_sort(input_list):
    """
    O(n*ln(n)) solution.
    :param input_list:
    :return:
    """
    input_list.sort()
    for i in range(len(input_list)-1):
        if input_list[i]==input_list[i+1]:
            return True
    return  False


if __name__=="__main__":
    test_input = [2,3,4,5,6,7,8,9,1,5]
    test_input2=[1,2,3,4,5,6,7,8,9,0]
    print(check_repeated(test_input))
    print(check_repeated(test_input2))

    print(check_repeated_sort(test_input))
    print(check_repeated_sort(test_input2))