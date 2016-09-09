"""
    Rearrange positive and negative numbers in an array containing mixed numbers both positive and negative in random order

"""



def rearrange_pos_neg(input_list):
    """
    Quick Sort based algorithm with time complexity - O(n)
    :param input_list:
    :return:
    """
    pivot = 0
    i = -1
    for j in range(len(input_list)):
        if input_list[j] < 0:
            i +=1
            input_list[i],input_list[j] = input_list[j],input_list[i]
    return input_list


if __name__=="__main__":
    input_list=[-1,4,5,6,7,-3,7,-2,9,-8]
    print(rearrange_pos_neg(input_list))
    


