
def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        key = i
        j=i-1
        while j >=0 and key<input_list[j]:
            input_list[j+1]=input_list[j]
            j-=1
        input_list[j+1]=key
    return input_list


def bucket_sort(input_list,DEFAULT_NUMBER_0F_BUCKETS):
    buckets = []
    for i in range(DEFAULT_NUMBER_0F_BUCKETS):
        buckets.append([])

    for i in range(len(input_list)):
        buckets[DEFAULT_NUMBER_0F_BUCKETS*input_list[i]].append(input_list[i])

    for bucket in buckets:
        insertion_sort(bucket)
    output_list = []

    for bucket in buckets :
        for i in bucket:
            output_list.append(bucket[i])
    return output_list

if __name__=="__main__":
    test = [23,12,65,78,22,24,62,76,98,15,17]
    print(bucket_sort(test,10))
