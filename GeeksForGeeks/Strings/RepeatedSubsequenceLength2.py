
"""
Repeated subsequence of length 2 or more

Given a string, find if there is any subsequence of length 2 or more that repeats itself such that
 the two subsequence don’t have same character at same position, i.e., any 0’th or 1st character in the
  two subsequences shouldn’t have the same index in the original string.

Example.

Input: ABCABD
Output: Repeated Subsequence Exists (A B is repeated)

Input: ABBB
Output: Repeated Subsequence Exists (B B is repeated)

Input: AAB
Output: Repeated Subsequence Doesn't Exist (Note that
A B cannot be considered as repeating because B is at
same position in two subsequences).

Input: AABBC
Output: Repeated Subsequence Exists (A B is repeated)

Input: ABCDACB
Output: Repeated Subsequence Exists (A B is repeated)

Input: ABCD
Output: Repeated Subsequence Doesn't Exist


"""

def create_hash(input_string) :
    if not input_string :
        return
    else :
        htable = {}
        for char in input_string :
            if not htable[char] :
                htable[char] = 1
            else :
                htable[char] += 1
        return htable

def check_palindrome(input_string):
    if not input_string :
        return True
    else :
        start = 0
        end = len(input_string)-1
        while start < end :
            if input_string[start] != input_string[end] :
                return False
            start += 1
            end -= 1
        return True

def check_repeated(input_string):
    if not input_string :
        return False
    else :

        htable = [0]*256
        for char in input_string :
            if htable[ord(char)] == 0 :
                htable[ord(char)] = 1
            else :
                htable[ord(char)] +=1
        start = 0
        for char in input_string :
            if htable[ord(char)] > 1 :
                input_string[start] = char
                start += 1
            if htable[ord(char)] >= 3 :
                return True

        repeated_string = input_string[:start]

        if check_palindrome(repeated_string) :

            if start & 1 :
                return repeated_string[start//2] == repeated_string[start//2 - 1]
            return False
        else :
            return True

if __name__=='__main__':
    str1 = 'ABCABD'
    print(check_repeated(list(str1)))

    str2 = 'ABBB'
    print(check_repeated(list(str2)))

    str3 = 'AAB'
    print(check_repeated(list(str3)))

    str4 = 'AABBC'
    print(check_repeated(list(str4)))

    str5 = 'ABCDACB'
    print(check_repeated(list(str5)))

    str6 = 'ABCD'
    print(check_repeated(list(str6)))