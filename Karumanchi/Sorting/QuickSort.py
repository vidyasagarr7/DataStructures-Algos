

def partition_end(list,start,end):
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




def quick_sort(input_list,start,end):
    """
    Quick Sort Algorithm for sorting an unordered list of numbers

    :param input_list:
    :param start:
    :param end:
    :return:
    """
    if start<end:
        part = partition_end(input_list,start,end)
        #part = partition_start(input_list,start,end)
        quick_sort(input_list,start,part-1)
        quick_sort(input_list,part+1,end)
        return input_list

if __name__=="__main__":
    test=[1,4,12,54,65,72,89,13,51,16,90]
    print(quick_sort(test,0,len(test)-1))

