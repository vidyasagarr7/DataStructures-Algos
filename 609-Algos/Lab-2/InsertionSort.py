
def insertion_sort(input_list):
    """
    InsertionSort Algorithm for sorting an unordered list of numbers
    :param input_list: unordered list of numbers
    :return: sorted list
    """

    for i in range(1,len(input_list)):
        key = input_list[i]
        j = i-1
        while j >= 0 and key < input_list[j]:
            input_list[j+1]=input_list[j]
            j-=1
        input_list[j+1] = key
    return input_list

if __name__=="__main__":
    test = [43,12,56,76,98,144,21,65,87,90]
    print(insertion_sort(test))


