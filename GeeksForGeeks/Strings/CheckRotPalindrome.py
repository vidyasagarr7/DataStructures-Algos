
"""
Check if a given string is a rotation of a palindrome

Given a string, check if it is a rotation of a palindrome.
 For example your function should return true for “aab” as it is a rotation of “aba”.

Examples:

Input:  str = "aaaad"
Output: 1
// "aaaad" is a rotation of a palindrome "aadaa"

Input:  str = "abcd"
Output: 0
// "abcd" is not a rotation of any palindrome.
"""

def check_palindrome(input_string):
    if not input_string :
        return
    else :
        left = 0
        right = len(input_string)-1
        while left < right :
            if input_string[left] != input_string[right] :
                return False
            else :
                left += 1
                right -= 1
        return True

def check_rot_palin(string):
    """
    O(n^2) solution.
    :param string:
    :return:
    """
    if not string :
        return False
    else :
        check_string = string + string
        for i in range(len(string)) :
            if check_palindrome(check_string[i:i+len(string)]):
                return True
        return False

if __name__=='__main__':
    test = 'aabaa'
    print(check_palindrome(test))

    test = 'aaaad'
    print(check_rot_palin(test))

    test = 'abcd'
    print(check_rot_palin(test))

    test = 'aaaad'
    print(check_rot_palin(test))