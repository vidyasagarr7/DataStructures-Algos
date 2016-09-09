
def merge(input_list,start,mid,end):
    """

    :param input_list:
    :param start:
    :param mid:
    :param end:
    :return:
    """
    first=mid-start+1
    second=end-mid
    left = [0]*first
    right = [0]*second

    for i in range(first):
        left[i]=input_list[start+i]
    for j in range(second):
        right[j]=input_list[mid+1+j]

    i=j=0
    k=start
    while  i<first and j<second:
        if left[i]<right[j]:
            input_list[k]=left[i]
            i+=1
            k+=1
        else :
            input_list[k]=right[j]
            j+=1
            k+=1
    while i <first :
        input_list[k]=left[i]
        i+=1
        k+=1
    while j<second:
        input_list[k]=right[j]
        j+=1
        k+=1
    return input_list

def merge_sort_rec(input_list,start,end):
    """

    :param input_list:
    :param start:
    :param end:
    :return:
    """

    if start<end:
        mid=(start+end)//2
        merge_sort_rec(input_list,start,mid)
        merge_sort_rec(input_list,mid+1,end)
        return merge(input_list,start,mid,end)

if __name__=="__main__":
    test = [23,12,65,78,22,24,62,76,98,15,17]
    print(merge_sort_rec(test,0,len(test)-1))
