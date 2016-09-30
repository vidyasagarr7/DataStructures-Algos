from Karumanchi.Sorting import QuickSort

def partition(list,start,end):
    """
    Partition Algorithm to partition a list - selecting the end element as the pivot.
    :param list:
    :param start:
    :param end:
    :return:
    """
    i=start-1
    pivot = list[end]
    for j in range(start,end):
        if list[j] <= pivot:
            i+=1
            list[i],list[j]=list[j],list[i]
    list[i+1],list[end]=list[end],list[i+1]
    return i+1


def _find_k_smallest(input_list,start,end,k):
    """
    Algorithm using partitioning for finding kth smallest number.
    :param input_list:
    :return:
    """

    if k>0 and k <= end-start+1:
        part = QuickSort.partition_end(input_list,start,end)
        if part-start == k-1:
            return input_list[part]
        elif part-start> k-1:
            return _find_k_smallest(input_list,start,part-1,k)
        else:
            return _find_k_smallest(input_list,part+1,end,k-part+start-1)
    return False

def find_k_smallest(input_list,k):
    return _find_k_smallest(input_list,0,len(input_list)-1,k)


def find_k_smallest_opt(input_list,k):
    """
    Median of medians.
    :param input_list:
    :param k:
    :return:
    """
    return 0

def find_median(input_list):
    """
    Algorithm to find the median of inputlist
    :param input_list:
    :return:
    """
    return find_k_smallest(input_list,len(input_list)//2)




if __name__=="__main__":
    test_input = [3,2,1,7,6,5,8,9,4,5,10,11,12,13,14,15]

    print(find_median(test_input))


