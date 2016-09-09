
def counting_sort(input_list,k):
    """

    :param input_list:
    :return:
    """

    output_list =  [0]*len(input_list)
    temp_list = [0]*k

    for j in range(len(input_list)):
        temp_list[input_list[j]]+=1

    for k in range(1,len(temp_list)):
        temp_list[k] += temp_list[k-1]

    for i in range(len(input_list)-1,-1,-1):
        output_list[temp_list[input_list[i]]-1] = input_list[i]
        temp_list[input_list[i]] -= 1

    return output_list

if __name__=="__main__":
    test = [23,12,23,23,12,12,65,78,22,24,62,76,98,15,76,98,17]
    print(counting_sort(test,100))













