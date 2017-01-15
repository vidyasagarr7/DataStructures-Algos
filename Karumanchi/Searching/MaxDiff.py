
"""
Find the max j-i such that A[j]>A[i].
"""

def find_maxdiff(input_list):
    """
    O(n^2) solution
    :param input_list:
    :return:
    """
    max_diff = 0
    for i in range(len(input_list)):
        #max_diff = ((j-i) for j in range(i+1,len(input_list)) if input_list[j]>input_list[i] and max_diff<(j-i))

        for j in range(i+1,len(input_list)):
            if input_list[j]>input_list[i] and max_diff < j-i :
                max_diff = j-i

    return max_diff



if __name__=="__main__":
    test = [34,8,10,3,2,80,30,33,1]
    print(find_maxdiff(test))

