from Karumanchi.Sorting import MergeSort

def delete_duplicates(input_list):
    sorted_list = MergeSort.merge_sort(input_list)
    i =0
    while i < len(sorted_list)-1:
        if sorted_list[i]==sorted_list[i+1]:
            sorted_list[i],sorted_list[len(sorted_list)-1] = sorted_list[len(sorted_list)-1],sorted_list[i]
            del sorted_list[len(sorted_list)-1]
        i+=1
    return sorted_list

def _delete_duplicates(input_list):
    foo  = set()
    for i in range(len(input_list)):
        foo.add(input_list[i])
    return foo

if __name__=="__main__":
    test = [2,2,4,6,8,4,3,2,6,7,8,9,0,1,2,5,8,2]
    print(_delete_duplicates(test))
