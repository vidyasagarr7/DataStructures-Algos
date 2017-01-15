

def inversion_count(input_list):
    """
    O(n^2) algorithm for finding number of inversions
    :param input_list:
    :return: number of inversions of the input list
    """
    count = 0
    for i in range(len(input_list)):
        for j in range(i,len(input_list)):
            if input_list[i]>input_list[j]:
                count+=1
    return count

 """
 ############# ---- USING MERGE SORT - INCOMPLETE ---- ###############

 """
def inversion_count_ms(input_list):
    """
    Merge Sort based algorithm to find inversion count.
    :param input_list:
    :return:
    """

    return _merge_sort(input_list,0,len(input_list)-1)


def _merge_sort(input_list,start,end):
    inv_count=0
    if start < end:
        mid = (start+end)//2
        inv_count = _merge_sort(input_list,start,mid)
        inv_count += _merge_sort(input_list,mid+1,end)
        inv_count += _merge(input_list,start,mid,end)
    return inv_count


def _merge(input_list,start,mid,end):
    first = mid-start+1
    second = end - mid
    left = [0]*first
    right = [0]*second
    for i in range(first):
        left[i]=input_list[start+i]
    for j in range(second):
        right[j]=input_list[mid+1+j]
    i=0
    j=0
    k=start
    inv_count = 0
    while i<first and j<second:
        if left[i] <= right[j]:
            input_list[k]=left[i]
            i+=1

        else:
            input_list[k]=right[j]
            j+=1
            inv_count+=1
        k+=1
    while i<first :
        input_list[k]=left[i]
        i+=1
        k+=1
        inv_count+=1
    while j<second:
        input_list[k]= right[j]
        j+=1
        k+=1

    return inv_count



if __name__=="__main__":
    test_input=[2, 4, 1, 3, 5]
    test_input2=[1, 20, 6, 4, 5]
    test_input3=[5,2,10,8,1,9,4,3,6,7]
    print("Number of inversions is : " + str(inversion_count(test_input)))

    print("Number of inversions using merge sort is : "+str(inversion_count_ms(test_input)))

    print("Number of inversions is : " + str(inversion_count(test_input2)))

    print("Number of inversions using merge sort is : "+str(inversion_count_ms(test_input2)))



    print("Number of inversions is : " + str(inversion_count(test_input3)))

    print("Number of inversions using merge sort is : "+str(inversion_count_ms(test_input3)))
