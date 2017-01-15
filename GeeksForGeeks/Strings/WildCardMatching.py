

"""
String matching where one string contains wildcard characters

Given two strings where first string may contain wild card characters and second string is a normal string.
Write a function that returns true if the two strings match. The following are allowed wild card characters
in first string.

* --> Matches with 0 or more instances of any character or set of characters.
? --> Matches with any one character.
For example, “g*ks” matches with “geeks” match. And string “ge?ks*” matches with “geeksforgeeks”
 (note ‘*’ at the end of first string). But “g*k” doesn’t match with “gee” as character ‘k’ is not
 present in second string.

"""

def match(str1,str2,first,second):
    if first == len(str1) and second == len(str2) :
        return True

    if first < len(str1) and second == len(str2) :
        return False

    if (first < len(str1) and str1[first] == '?' ) or (first<len(str1) and second < len(str2) and
                                                       str1[first]==str2[second]) :
        return match(str1,str2,first+1,second+1)

    if first < len(str1) and str1[first] == '*' :
        return match(str1,str2,first,second+1) or match(str1,str2,first+1,second+1)

    return False

if __name__=='__main__':
    print(match('g*ks','geeksforgeeks',0,0))
    print(match('ge?ks','geeks',0,0))
    print(match('g?ek*','geeksforgeeks',0,0))
    print(match('*p','geeks',0,0))





