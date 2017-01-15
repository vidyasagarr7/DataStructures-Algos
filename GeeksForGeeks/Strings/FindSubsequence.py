

"""
Given two strings, find if first string is a subsequence of second

Given two strings str1 and str2, find if str1 is a subsequence of str2.
A subsequence is a sequence that can be derived from another sequence by deleting some
elements without changing the order of the remaining elements (source: wiki). Expected time complexity is linear.

Examples:

Input: str1 = "AXY", str2 = "ADXCPY"
Output: True (str1 is a subsequence of str2)

Input: str1 = "AXY", str2 = "YADXCP"
Output: False (str1 is not a subsequence of str2)

Input: str1 = "gksrek", str2 = "geeksforgeeks"
Output: True (str1 is a subsequence of str2)
"""

def check_substring(str1,str2,first,second):
    if len(str1) == 0 or first == len(str1):
        return True
    if second == len(str2) :
        return False
    else :
        if first < len(str1) and second < len(str2) and str1[first] == str2[second] :
            return check_substring(str1,str2,first+1,second+1)
        else :
            return check_substring(str1,str2,first,second+1)

def check_substring_iter(string1,string2):
    if len(string1)==0 :
        return True
    else :
        first = 0
        second = 0
        while first < len(string1) and second < len(string2) :
            if string1[first] == string2[second] :
                first += 1
            second += 1

        if first == len(string1):
            return True
        else :
            return False

if __name__=='__main__':
    string1 = 'axy'
    string2 = 'adxcpy'
    print(check_substring(list(string1),list(string2),0,0))

    print(check_substring_iter(list(string1),list(string2)))

    string1 = 'axy'
    string2 = 'yadxcp'
    print(check_substring(list(string1),string2,0,0))

    print(check_substring_iter(list(string1),list(string2)))

    string1 = 'gksrek'
    string2 = 'geeksforgeeks'
    print(check_substring(string1,string2,0,0))

    print(check_substring_iter(list(string1),list(string2)))
