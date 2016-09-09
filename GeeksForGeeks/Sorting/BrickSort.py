
def brick_sort(input_list):
    """
    Bubble Sort based algorithm that sorts odd and even indices separately.
    :param input_list:
    :return: sorted list.
    """
    is_sorted = False

    while not is_sorted :
        is_sorted=True
        # Even Sort
        for i in range(0,len(input_list)-2,2):
            if input_list[i] > input_list[i+1]:
                input_list[i],input_list[i+1]=input_list[i+1],input_list[i]
                is_sorted=False
        # odd sort
        for i in range(1,len(input_list)-2,2):
            if input_list[i] > input_list[i+1]:
                input_list[i],input_list[i+1]=input_list[i+1],input_list[i]
                is_sorted=False

    return input_list

if __name__=="__main__":
    test_input=[2,5,3,7,5,9,1,6]
    print(brick_sort(test_input))