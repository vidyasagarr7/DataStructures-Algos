
def check_pairwise_sorted(input_list):

    """
    O(n) time - Check if each successive pair of elements are pairwise sorted
    :param input_list:
    :return:
    """

    return all(input_list[i] < input_list[i+1] for i in range(0,len(input_list)-1,2))

if __name__=="__main__":
    test = [34,48,10,13,2,80,30,35]
    test1 = [34,48,10,13,2,80,30,23]
    print(check_pairwise_sorted(test1))
    print(check_pairwise_sorted(test))
