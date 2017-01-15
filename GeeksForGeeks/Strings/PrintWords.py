
"""
Recursively print all sentences that can be formed from list of word lists
Given a list of word lists How to print all sentences possible taking one word from a list at a time via recursion?

Example:

Input: {{"you", "we"},
        {"have", "are"},
        {"sleep", "eat", "drink"}}

Output:
  you have sleep
  you have eat
  you have drink
  you are sleep
  you are eat
  you are drink
  we have sleep
  we have eat
  we have drink
  we are sleep
  we are eat
  we are drink
"""

def print_words(strings_list):
    if not strings_list :
        return
    else :
        out = []
        for i in range(len(strings_list)) :



