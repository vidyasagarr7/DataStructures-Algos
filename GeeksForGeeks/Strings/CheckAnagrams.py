
"""

Check whether two strings are anagram of each other
Write a function to check whether two given strings are anagram of each other or not.

An anagram of a string is another string that contains same characters, only the order of characters can be
different. For example, “abcd” and “dabc” are anagram of each other.

"""

NO_CHARS = 256
def check_anagrams(string1,string2):
    if (not string1 and string2) or (string1 and not string2):
        return False
    else :

        if len(string1) != len(string2) :
            return False
        htable = [0]*NO_CHARS
        for ch in string1 :
            htable[ord(ch)] += 1
        for ch2 in string2 :
            htable[ord(ch2)] -= 1
        for ch in string1 :
            if htable[ord(ch)] != 0 :
                return False
        return True


if __name__=='__main__':
    one = 'abcd'
    two = 'dabc'
    print(check_anagrams(one,two))

    two = 'dabcddfd'
    print(check_anagrams(one,two))
