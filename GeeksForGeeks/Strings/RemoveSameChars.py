"""
Remove characters from the first string which are present in the second string

"""

def remove_same_chars(string1,string2):
    if len(string1)==0 and string2  or len(string2)==0 and string1 :
        return string1 if len(string2)==0 else string2
    else  :
        NO_CHARS = 256
        list1 = list(string1)
        list2 = list(string2)
        hash_table = [0]*(NO_CHARS)

        for ch in list2 :
            hash_table[ord(ch)] += 1
        start = 0
        for i in range(len(list1)):
            if hash_table[ord(list1[i])] == 0 :
                list1[start] = list1[i]
                start += 1
        return ''.join(list1[:start])
        """
        for ch in list1 :
            if hash_table[ord(ch)] == 0 :
                print(ch)
        """
if __name__=='__main__':
    string1 = 'test string'
    string2 = 'mask'
    print(remove_same_chars(string1,string2))
    str1 = 'geeksforgeeks'
    print(remove_same_chars(str1,string2))

