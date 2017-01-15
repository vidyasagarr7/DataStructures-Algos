
def heapify(input_list,index):
    left = 2*index+1
    right = 2*index+2
    largest = index

    if left<=len(input_list) and input_list[left] >= input_list[largest]:
        largest=left
    if right<=len(input_list) and input_list[right]>=input_list[largest]:
        largest=right
    if largest!=index:
        swap(input_list,largest,index)
        heapify(input_list,largest)

def swap(input_list,index1,index2):
    input_list[index1],input_list[index2]=input_list[index2],input_list[index1]
    return input_list

def build_max_heap(input_list):
    for i in range(len(input_list)//2,0,-1):
        heapify(input_list,i)

