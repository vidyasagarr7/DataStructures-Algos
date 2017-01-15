
def bubble_sort(input_list):
    """
    Bubble Sort algorithm to sort an unordered list of numbers

    :param input_list: unsorted list of numbers
    :return: sorted list
    """

    for i in range(len(input_list)):
        for j in range(len(input_list)-1-i):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
    return input_list

if __name__=="__main__":
    test = [23,25,12,14,17,85,98,34,32,109,56]
    print(bubble_sort(test))