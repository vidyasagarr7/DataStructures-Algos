"""
Partition an array into 3 sets.

"""

def three_way_partition(input_list,mid):
    """
    O(n) - time. 
    3-way partition in a list - DNF based algorithm
    :param input_list:
    :param mid:
    :return:
    """
    left = 0
    right = len(input_list)-1
    current  = 0
    while current <= right :
        if input_list[current] < mid:
            input_list[current],input_list[left] = input_list[left],input_list[current]
            current +=1
            left +=1
        elif input_list[current] > mid :
            input_list[right],input_list[current] = input_list[current],input_list[right]
            right -=1
        else :
            current += 1
    return input_list

if __name__ =="__main__":
    test = [0,0,0,1,1,1,0,0,1,0,1,0,2,0,2,0,1,2,1,0,1,2,2,1,2,1,2,1,0,1,2,0,1,2,0,1,2,0]
    test1 = [0,0,0,1,1,1,0,0,1,0,1,0,2,0,2,0,1,2,1,0,1,2,2,1,2,1,2,1,0,1,2,0,1,2,0,1,2,0,5,4,3,6,8,9,0,3,2]
    print(three_way_partition(test,1))
    print(three_way_partition(test1,1))