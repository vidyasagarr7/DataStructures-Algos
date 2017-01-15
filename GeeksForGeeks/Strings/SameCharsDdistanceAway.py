
"""
Rearrange a string so that all same characters become d distance away

Given a string and a positive integer d. Some characters may be repeated in the given string.
 Rearrange characters of the given string such that the same characters become d distance away from each other.
  Note that there can be many possible rearrangements, the output should be one of the possible rearrangements.
  If no such arrangement is possible, that should also be reported.
Expected time complexity is O(n) where n is length of input string.

Examples:
Input:  "abb", d = 2
Output: "bab"

Input:  "aacbbc", d = 3
Output: "abcabc"

Input: "geeksforgeeks", d = 3
Output: egkegkesfesor

Input:  "aaa",  d = 2
Output: Cannot be rearranged

"""

class CharFreq:
    def __init__(self,char,freq):
        self.c = char
        self.f = freq

def rearrange(input_string):
    if not input_string :
        return
    else :
        htable = {}
        for char in input_string :
            if char not in htable :
                htable[char] = 1
            else :
                htable[char] += 1


