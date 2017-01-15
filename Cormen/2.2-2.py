
def selection_sort(input_list):
    """
    Selection Sort to sort an unsorted list
    :param input_list: unsorted list
    :return: sorted list
    """

    for i in range(len(input_list)-1):
        min_idx = i
        for j in range(i+1,len(input_list)):
            if input_list[j] < input_list[min_idx]:
                min_idx = j
            j -= 1
        input_list[i],input_list[min_idx] = input_list[min_idx], input_list[i]
    return input_list

if __name__=="__main__":
    test_list = [42,23,12,543,65,745,752,542,64,65,75]
    print(selection_sort(test_list))
