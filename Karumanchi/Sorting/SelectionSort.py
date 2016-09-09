

def selection_sort(input_list):
    """
    Selection sort algorithm to sort an unsorted list

    Algorithm :
    - Find the minimum value in the lst
    - swap it with the current value in the list
    - repeat this process for all elements till the list is sorted

    :param input_list:
    :return:
    """


    for i in range(len(input_list)-1):
        min_idx = i
        for j in range(i+1,len(input_list)):
            if input_list[min_idx]>input_list[j]:
                min_idx = j
        input_list[min_idx],input_list[i] = input_list[i],input_list[min_idx]
    return input_list


if __name__=="__main__":
    test = [23,12,65,78,22,24,62,76,98,15,17]
    print(selection_sort(test))
