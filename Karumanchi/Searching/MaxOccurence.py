from Karumanchi.Sorting import MergeSort

def max_occurece(input_list):
    """
    O(n^2) implementation for finding the element that occurs max number of times.
    :param input_list:
    :return:
    """
    if not input_list :
        return
    max_count=0
    max_element = input_list[0]
    for i in range(len(input_list)):
        count=1
        for j in range(i+1,len(input_list)):
            if input_list[i]==input_list[j]:
                count+=1
        if count > max_count:
            max_count = count
            max_element = input_list[i]
    return max_count,max_element

def max_occurance_opt(input_list):
    """
    O(n*log(n)) algorithm
    :param input_list:
    :return:
    """
    sorted_list = MergeSort.merge_sort(input_list)
    max_idx = 0
    count = 1
    max_count =0
    for i in range(len(sorted_list)-1):
        if sorted_list[i]==sorted_list[i+1]:
            count+=1
        else:
            count=1
        if max_count < count:
            max_count = count
            max_idx=i
    return max_count,sorted_list[max_idx]

def _max_occurance_opt(input_list):
    """
    O(n) algorithm - use hashing. O(n) space.
    :param input_list:
    :return:
    """
    table = {}
    maximum = 0
    max_element = 0
    for element in input_list:
        if element in table:
            table[element] +=1
        elif element != "":
            table[element] =1
        else : table[element] = 0

    for element in table :
        if table[element] > maximum:
            maximum = table[element]
            max_element = element
    return max_element, maximum

def max_occur(input_list):
    """
    Assume that the elements are in the range n-1
    :param input_list:
    :return:
    """
    maximum = 0
    max_idx = 0
    n=len(input_list)
    temp = [0]*n
    for i in range(n):
        temp[i] = input_list[i]
    for i in range(n):
        input_list[input_list[i]%n]+= n
    for i in range(n):
        if input_list[i]//n > maximum:
            maximum = input_list[i]//n
            max_idx = i

    return maximum,max_idx




##### Revisit this problem, have to return the value of the element that occurs maximum numer of times.
def __max_occurance(input_list,n):
    """
    Assuming the elements are in the range 0-(n-1) - similar to counting sort
    :param input_list:
    :return:
    """
    temp_list = [0]*n

    for i in range(len(input_list)):
        temp_list[input_list[i]] += 1

    for i in range(1,len(temp_list)):
        temp_list[i] += temp_list[i-1]

    max_diff = 0
    max_idx = 0
    print(temp_list)
    for i in range(1,len(temp_list)):
        if temp_list[i]-temp_list[i-1] > max_diff :
            max_diff = temp_list[i]-temp_list[i-1]
            max_idx = i

    return max_diff



if __name__=="__main__":
    test = [1,2,3,5,6,7,7,4,7,7,8,8,8,4,4,4,4,4,4,5]
    print(len(test))
    print(max_occurece(test))

    test = [1,2,3,5,6,7,7,4,7,7,8,8,8,4,4,4,4,4,4,5]
    print(max_occurance_opt(test))

    test = [1,2,3,5,6,7,7,4,7,7,8,8,8,4,4,4,4,4,4,5]

    print(_max_occurance_opt(test))
    test = [1,2,3,5,6,7,7,4,7,7,8,8,8,4,4,4,4,4,4,5]

    print(max_occur(test))


