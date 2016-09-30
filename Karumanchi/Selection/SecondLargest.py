
def find_second_largest(input_list):

    maximum = input_list[0]
    max_idx = 0
    for i in range(1,len(input_list)):
        if input_list[i] > maximum:
            maximum = input_list[i]
            max_idx=i
    input_list.pop(max_idx)
    second_maximum = input_list[0]
    for i in range(1,len(input_list)):
        if input_list[i]>second_maximum:
            second_maximum = input_list[i]
    return second_maximum



if __name__=="__main__":
    test_input=[2,5,7,9,1,6,8]
    print(find_second_largest(test_input))
