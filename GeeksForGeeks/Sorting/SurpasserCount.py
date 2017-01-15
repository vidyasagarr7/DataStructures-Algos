
"""
    ################   ALGORITHM INCOMPLETE  ##################
"""


def surpasser_count(input_list):
    """
    O(n^2) algorithm for finding the surpassing count of each element in the list
    :param input_list:
    :return:
    """

    output_list =[0]*len(input_list)
    for i in range(len(input_list)):
        for j in range(i,len(input_list)):
            if input_list[i] < input_list[j]:
                output_list[i]+=1
    return output_list

if __name__=="__main__":
    input_test=[2, 7, 5, 3, 0, 8, 1]
    print(surpasser_count(input_test))