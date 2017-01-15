"""
Print all the duplicates in the input string

"""

def print_duplicates(input_string):
    if len(input_string)==0 :
        return
    else :
        dictionary = {}
        for i in range(len(input_string)):
            if input_string[i] not in dictionary:
                dictionary[input_string[i]] = 1
            else :
                dictionary[input_string[i]] +=1
        for key, value in dictionary.items():
            if value > 1:
                print('key {} and value {}'.format(key,value))

def _print_duplicates(input_string):
    NO_CHARS = 256
    if len(input_string)==0 :
        return
    else :
        hash_table = [0]*NO_CHARS

        for ch in input_string :
            hash_table[ord(ch)] += 1


        for i in range(len(hash_table)) :
            if hash_table[i] > 1 :
                print('key {} and value {}'.format(chr(i),hash_table[i]))


if __name__=='__main__':

    string = 'geeksforgeeks'

    print_duplicates(string)

    _print_duplicates(string)