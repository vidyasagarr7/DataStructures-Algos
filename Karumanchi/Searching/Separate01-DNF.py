"""
Dutch National Flag algorithm - separate 0's and 1's in an array

Algo :
    - start with left = 0 and right - (n-1)
    - increment till left index untill it is 1
    - decrement till right index untill it is 0
    - if left < right : swap(left,right)
"""

def seperate_two_kind(input_list):
    """
    separate 0's and 1's
    :param input_list:
    :return:
    """
    left = 0
    right = len(input_list)-1

    while left < right :
        while input_list[left] != 1 and left<right:
            left += 1
        while input_list[right] !=0 and left<right:
            right -=1
        if left < right :
            input_list[left],input_list[right] = input_list[right],input_list[left]
            left +=1
            right -=1
    return input_list

def _seperate_two_kinds(input_list):
    """
    separate 0's and 1's - different way of solving
    :param input_list:
    :return:
    """
    summation = 0
    for i in range(len(input_list)):
        summation +=1
    for i in range(len(input_list)):
        if i < len(input_list)-summation:
            input_list[i]=0
        else :
            input_list[i]=1
    return input_list


if __name__=="__main__":
    test = [1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0]
    print(seperate_two_kind(test))

    print(_seperate_two_kinds())