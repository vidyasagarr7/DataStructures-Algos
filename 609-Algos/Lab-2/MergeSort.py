

def merge(input_list,start,mid,end):
    """
    Merge algorithm to merge two sorted sub-arrays(lists)
    :param input_list:
    :param start:
    :param mid:
    :param end:
    :return:
    """
    first = mid-start+1
    second = end-mid
    left = [0]*first
    right = [0]*second
    for i in range(first):
        left[i]=input_list[start+i]
    for j in range(second):
        right[j]=input_list[mid+1+j]
    i=j=0
    k=start
    while i<first and j<second:
        if left[i]<right[j]:
            input_list[k]=left[i]
            i+=1
        else:
            input_list[k]=right[j]
            j+=1
        k+=1
    while i<first :
        input_list[k]=left[i]
        i+=1
        k+=1
    while j<second:
        input_list[k]=right[j]
        j+=1
        k+=1
    return input_list

def merge_sort(input_list,start,end):
    """
    Merge Sort Algorithm for sorting an unordered list of numbers
    :param input_list: unsorted list of numbers
    :param start: start point in list
    :param end: end point in the list
    :return: sorted list
    """
    if start < end:
        mid=(start+end)//2
        merge_sort(input_list,start,mid)
        merge_sort(input_list,mid+1,end)
        return merge(input_list,start,mid,end)


if __name__=="__main__":
    test = [23,12,65,78,22,24,62,76,98,15,17,38,1999]
    print(merge_sort(test,0,len(test)-1))