from GeeksForGeeks.Strings.LPS import find_lps
"""
Find all distinct palindromic sub-strings of a given string
Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.

Examples:

Input: str = "abaaa"
Output:  Below are 5 palindrome sub-strings
a
aa
aaa
aba
b


Input: str = "geek"
Output:  Below are 4 palindrome sub-strings
e
ee
g
k
"""


def distinct_substrings(input_string):

    if not input_string :
        return
    else :
        htable = {}
        start = 0

        for char in input_string :





