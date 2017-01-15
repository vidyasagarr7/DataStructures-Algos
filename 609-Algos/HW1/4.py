import math
"""
    Find two missing elements in an array with numbers from 0 to n

"""

def find_missing(input_list):
    """
    O(n^2) algorithm
    :param input_list:
    :return:
    """

    """
    out_list=[]
    for i in range(len(input_list)+2):
        if i not in input_list:
            out_list.append(i)
    return out_list
    """

    summation = 0
    product1=1
    product2 = 1
    for i in range(1,len(input_list)+2):
        if i < len(input_list):
            summation += input_list[i]
            product1 *= input_list[i]
        product2 *= i

    summ2 = ((len(input_list)+2)*(len(input_list)+3)/2)-summation
    prod2 = product2/product1
    t = prod2*prod2-4*summ2
    return (prod2 + math.sqrt(t))/2, (prod2-math.sqrt(t))/2



if __name__=="__main__":
    test = [2,10,9,4,7,8,1,6]
    print(find_missing(test))