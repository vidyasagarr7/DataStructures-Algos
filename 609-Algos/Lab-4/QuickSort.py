

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

if __name__=="__main__":
    test = [12,45,76,98,46,90,26,49]
    print(quick_sort(test,0,len(test)-1))
