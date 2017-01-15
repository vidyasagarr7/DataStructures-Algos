"""

Given a string, recursively remove adjacent duplicate characters from string. The output string should not have any
 adjacent duplicates. See following examples.

Input:  azxxzy
Output: ay
First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates,
so it is further reduced to "ay".

Input: geeksforgeeg
Output: gksfor
First "geeksforgeeg" is reduced to "gksforgg". The string "gksforgg" contains
duplicates, so it is further reduced to "gksfor".

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac


"""

def remove_duplicates(string):
    if not string:
        return
    else :
        i = 0
        j = 0
        prev = ''
        while i < len(string) :
            if i < len(string)-1  and string[i] == string[i+1] :
                prev = string[i]
                i += 2
            elif prev == string[i] :
                i += 1
            elif j >= 1 and string[j-1] == string[i] :
                j -= 1
                i += 1
            else:
                string[j] = string[i]
                i +=1
                j +=1
        return ''.join(string[:j])



if __name__=='__main__':
    string = list('geeksforgeeg')
    print(remove_duplicates(string))

    string = 'azxxzy'
    print(remove_duplicates(list(string)))

    string = 'caaabbbaacdddd'
    print(remove_duplicates(list(string)))

    string = 'acaaabbbacdddd'
    print(remove_duplicates(list(string)))
