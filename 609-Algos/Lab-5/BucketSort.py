import math

BUCKET_SIZE=3



def partition(input_array,start,end):
    pivot = input_array[end]
    i = start-1
    for j in range(start,end):
        if input_array[j]<pivot:
            i+=1
            input_array[j],input_array[i]=input_array[i],input_array[j]

    input_array[i+1],input_array[end]=input_array[end],input_array[i+1]
    return i+1



def quick_sort(input_array,start,end):
    """
    Quick Sort implementation for sorting a list - O(nln(n)) time
    :param input_array:
    :param start:
    :param end:
    :return:
    """

    if start<end:
        q = partition(input_array,start,end)
        quick_sort(input_array,start,q-1)
        quick_sort(input_array,q+1,end)
        return input_array

def _quicksort(input_array):
    return quick_sort(input_array,0,len(input_array)-1)

def bucket_sort(input_list, bucketSize=1):
    """

    :param input_list:
    :param bucketSize: default bucket size
    :return:
    """
    if len(input_list) == 0:
        return input_list

    min_value = min(input_list)
    max_value = max(input_list)

    # initialization of buckets
    bucket_count = math.floor((max_value - min_value) / bucketSize) + 1
    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])

    #  input values into the buckets
    for i in range(0, len(input_list)):
        buckets[math.floor((input_list[i] - min_value) / bucketSize)].append(input_list[i])


    input_list = []
    for i in range(0, len(buckets)):
        _quicksort(buckets[i])
        for j in range(0, len(buckets[i])):
            input_list.append(buckets[i][j])

    return input_list

if __name__=='__main__':
    input_list = [2,4,1,3,5,6,9,6,7,8,10]
    print(bucket_sort(input_list,BUCKET_SIZE))