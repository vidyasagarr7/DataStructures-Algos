"""
Find the smallest window in a string containing all characters of another string

Given two strings string1 and string2, find the smallest substring in string1 containing all characters of
string2 efficiently.

For Example:

Input string1: “this is a test string”
Input string2: “tist”
Output string: “t stri”

"""

def build_hashtable(string):
    hashtable = {}
    for ch in string :
        if ord(ch) in hashtable :
            hashtable[ord(ch)] += 1
        else :
            hashtable[ord(ch)] = 1
    return hashtable

def smallest_window(str1,str2):

    hash_table = {}
    count = 0

    for i in range(len(str1)):

