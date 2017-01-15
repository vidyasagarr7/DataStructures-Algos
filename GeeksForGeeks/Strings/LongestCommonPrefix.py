

"""
Longest Common Prefix | Set 1 (Word by Word Matching)
Given a set of strings, find the longest common prefix.

Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output : "gee"

Input  : {"apple", "ape", "april"}
Output : "ap"
"""

def lcp(string_list):
    """
    Word by word comparison algorithm
    :param string_list:
    :return:
    """
    if not string_list :
        return
    else :
        temp  = string_list[0]
        prev_end = len(temp)
        for i in range(1,len(string_list)):
            prev_end = find_common(temp,string_list[i],prev_end)
        return ''.join(temp[:prev_end])

def find_common(str1,str2,prev_end):

    if not str1 or not str2 :
        return
    else :
        start  = 0
        for i in range(min(prev_end,len(str2))) :
            if str1[i] != str2[i] :
                break
            else :
                start += 1
        return start


def find_minlen(string_list):
    if not string_list :
        return 0
    else :
        min_len = len(string_list[0])
        for string in string_list :
            if len(string) < min_len :
                min_len = len(string)
        return min_len

def _lcp(string_list):
    """
    Character by character comparison algorithm
    :param string_list:
    :return:
    """
    if not string_list :
        return
    else :
        min_length = find_minlen(string_list)
        result = ['0']*min_length
        start = 0
        for i in range(min_length) :
            char = string_list[0][i]

            for string in string_list :
                if string[i] != char :
                    return ''.join(result[:start])
            result[start] = char
            start += 1



if __name__=='__main__':
    string_list = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
    print(lcp(string_list))

    print(_lcp(string_list))

    string_list = ['apple','ape','april']
    print(lcp(string_list))

    print(_lcp(string_list))
