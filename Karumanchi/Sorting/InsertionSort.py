

def insertion_sort(input_list):
    """
    Insertion Sort algorithm to sort a list of numbers

    Algo :
    - every loop in the list, remove the present item and insert into the sorted list before it.

    :param input_list:
    :return:
    """

    for i in range(1,len(input_list)):
        key = input_list[i]
        print("set key = {}".format(str(key)))
        j=i
        print("check if key :{} is less than element :{}".format(str(key),str(input_list[j-1])))
        while j>0 and key < input_list[j-1]:
            print("moving the element :{} to position: {}".format(str(input_list[j - 1]),j))
            input_list[j] = input_list[j-1]
            j-=1
        print("inserting the key : {} at position: {}".format(str(key),j))
        input_list[j]=key
        print("Array after the operation : {}".format(input_list))
    return input_list

if __name__=="__main__":
    test = [23,12,65,78,22,24,62,76,98,15,17]
    test2 = [31,41,59,26,41,51]
    print(insertion_sort(test2))
