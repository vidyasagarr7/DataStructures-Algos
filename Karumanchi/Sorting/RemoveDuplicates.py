
from Karumanchi.Sorting import MergeSort
def remove_duplicates(input_list):
    temp = []
    sorted_list = MergeSort.merge_sort(input_list)
    temp.append(input_list[0])
    for i in range(1,len(sorted_list)):
        if sorted_list[i] == sorted_list[i-1]:
            continue
        else :
            temp.append(sorted_list[i])
    return temp

if __name__=="__main__":
    test = [1,1,1,2,2,3,4,5,6,1,2]
    print(remove_duplicates(test))