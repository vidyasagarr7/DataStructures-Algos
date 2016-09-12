
def find_max_repetition_element(input_list):
    """
    O(n^2) solution for finding a max repeated element in the input list
    :param input_list:
    :return:
    """

    max_count=0
    max_id=-1

    for i in range(len(input_list)):
        count =1
        for j in range(i+1,len(input_list)):
            if input_list[i]==input_list[j]:
                count+=1
        if max_count <= count:
            max_count = count
            max_id=i
    if max_count==1:    # returns the first element if there are no repetitions.
        max_id=0
    return max_count, max_id



def max_repetitions(input_list):
    """
    O(n*ln(n)) algorithm to find the max repeated element.
    :param input_list:
    :return:
    """
    input_list.sort()

    max_count=0
    count=1
    max_id=0
    for i in range(len(input_list)-1):
        if input_list[i]==input_list[i+1]:
            count+=1
        else:
            count=1
        if max_count <= count:
            max_count=count
            max_id=i
    return max_count,max_id



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

def max_rep(input_list):
    """
    Taking a preassumption that the input list of values lies in a range, then the problem can be solved in linear time.
    Sorting and finding count in linear time - O(n)
    :param input_list:
    :return:
    """
    out = counting_sort(input_list,10)

    max_count=0
    count=1
    max_id=0

    for i in range(len(input_list)-1):
        if input_list[i]==input_list[i+1]:
            count+=1
        else:
            count =1
        if max_count <= count:
            max_count=count
            max_id=i
    return max_count,max_id



if __name__=="__main__":
    test_input1=[2,3,2,2,2,5,5,6,8,7,8,3,2,6,7,8,4,2,7,8,2,2,2,6,4,7,8,9]
    test_input2=[1,2,3,4,5,6,7,8,9]

    count,index = find_max_repetition_element(test_input1)
    print(count,test_input1[index])
    count2,index2 = find_max_repetition_element(test_input2)
    print(count2,test_input2[index2])

    count3, index3 = max_repetitions(test_input1)
    print(count3, test_input1[index3])
    count4, index4 = max_repetitions(test_input2)
    print(count4, test_input2[index4])

    count5, index5 = max_rep(test_input1)
    print(count5,test_input1[index5])
    count6, index6 = max_rep(test_input2)
    print(count6,test_input2[index6])




