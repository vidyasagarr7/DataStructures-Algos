"""
    Rearrange positive and negative numbers in an array containing mixed numbers both positive and negative in random orde

"""



def rearrange_pos_neg(input_list):
    """
    Quick Sort based algorithm with time complexity - O(n)
    :param input_list:
    :return:
    """
    pivot = 0
    i = -1
    for j in range(len(input_list)):
        if input_list[j] < 0:
            i +=1
            input_list[i],input_list[j] = input_list[j],input_list[i]
    return input_list


def merge(input_list,start,mid,end):

    first = mid-start+1
    second = end-mid
    left = [0]*first
    right = [0]*second
    for i in range(first):
        left[i]=input_list[start+i]
    for j in range(second):
        right[j]=input_list[mid+1+j]

    i=0
    j=0
    k=start

    while i < first and left[i]<0:
        input_list[k] = left[i]
        k+=1
        i+=1
    while j < second and right[j]<0:
        input_list[k]=right[j]
        j+=1
        k+=1
    i=0
    j=0
    while i<first and left[i]>0:
        input_list[k]=left[i]
        i+=1
        k+=1
    while j<second and right[j]>0:
        input_list[k]=right[j]
        j+=1
        k+=1
    return input_list


def rearrange_pos_neg_ms(input_list,start,end):
    """
    Merge sort based algorithm
    :param input_list:
    :return:
    """
    if start<end:
        mid = (start+end)//2
        rearrange_pos_neg_ms(input_list,start,mid)
        rearrange_pos_neg_ms(input_list,mid+1,end)
        return merge(input_list,start,mid,end)




if __name__=="__main__":
    input_list=[-1,4,5,6,7,-3,7,-2,9,-8]
    #print(rearrange_pos_neg(input_list))
    print(rearrange_pos_neg_ms(input_list,0,len(input_list)))


