"""
Remove all duplicates from a given string

"""

def remove_duplicates(input_string):
    """
    O(n*logn) algorithm

    :param input_string:
    :return:
    """

    if len(input_string) == 0 :
        return input_string
    else:

        input_list = list(input_string)

        input_list.sort()

        start = 1

        # inplace addition of unique characters from starting
        for i in range(1,len(input_list)):
            if input_list[i]!=input_list[i-1] :
                input_list[start] = input_list[i]
                start +=1
        return input_list[:start]

def _remove_duplicates(input_string):
    """
    O(n) time algorithm
    :param input_string:
    :return:
    """

    if len(input_string) ==0 or len(input_string)==1 :
        return input_string
    else :
        NO_CHARS = 256
        input_list = list(input_string)
        hash_table = [0]*NO_CHARS

        start = 0

        for i in range(len(input_list)):
            if hash_table[ord(input_list[i])] == 0 :
                hash_table[ord(input_list[i])] = 1
                input_list[start] = input_list[i]
                start +=1

        return input_list[:start]



if __name__=='__main__':
    string = 'geeksforgeeks'
    print(remove_duplicates(string))
    print(_remove_duplicates(string))
