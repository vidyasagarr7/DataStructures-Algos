

"""
In-place replace multiple occurrences of a pattern

Given a string and a pattern, replace multiple occurrences of a pattern by character ‘X’.
The conversion should be in-place and solution should replace multiple consecutive (and non-overlapping)
 occurrences of a pattern by a single ‘X’.

String – GeeksForGeeks
Pattern – Geeks
Output: XforX

String – GeeksGeeks
Pattern – Geeks
Output: X

String – aaaa
Pattern – aa
Output: X

String – aaaaa
Pattern – aa
Output: Xa
"""

def compare(str1,pattern,index):
    length = len(pattern)
    if index + length > len(str1) :
        return False
    for i in range(index,index+length) :
        a = str1[i]
        b = pattern[i-index]
        if str1[i] != pattern[i-index] :
            return False
    return True

def inplace_replace(input_string,pattern):
    if not input_string :
        return
    else :
        length = len(pattern)
        j = 0
        i = 0
        while i < len(input_string) :
            if compare(input_string,pattern,i) :
                if j > 0 and input_string[j-1] == 'X' :
                    i += length
                    continue
                else :
                    input_string[j] = 'X'
                    i = i + length
            else :
                input_string[j] = input_string[i]
                i += 1
            j += 1
        return input_string[:j]

if __name__=='__main__' :
    test = 'GeeksForGeeks'
    pattern = 'Geeks'
    print(inplace_replace(list(test),list(pattern)))

    test = 'GeeksGeeks'
    pattern = 'Geeks'
    print(inplace_replace(list(test),list(pattern)))

    test = 'aaaa'
    pattern = 'aa'
    print(inplace_replace(list(test),list(pattern)))

    test = 'aaaaa'
    pattern = 'aa'
    print(inplace_replace(list(test),list(pattern)))






