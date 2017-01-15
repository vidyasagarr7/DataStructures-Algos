


def build_max_heap(input_array):
    heap_size = len(input_array)
    for i in range(heap_size//2,-1,-1):
        max_heapify(input_array,heap_size,i)

def max_heapify(input_array,heap_size,index):

    print(input_array[index-1])
    largest = index
    left_index = 2*index+1
    right_index = 2*index+2

    if left_index<heap_size and input_array[left_index]>input_array[largest]:
        largest=left_index

    if right_index<heap_size and input_array[right_index]>input_array[largest]:
        largest=right_index

    if largest != index:
        input_array[largest],input_array[index]=input_array[index],input_array[largest]
        max_heapify(input_array,heap_size,largest)

def heap_sort(input_array):
    """
    HeapSort algorithm for sorting - O(n*ln(n)) time complexity.
    :param input_array:
    :return:
    """

    build_max_heap(input_array)

    for i in range(len(input_array)-1,0,-1):
        input_array[i],input_array[0]=input_array[0],input_array[i]
        max_heapify(input_array,i,0)

    return input_array
if __name__=="__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print(heap_sort(arr))
