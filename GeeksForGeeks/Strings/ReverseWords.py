
"""
Reverse words in a given string

Example: Let the input string be “i like this program very much”.
The function should change the string to “much very program this like i”

"""

def reverse_words(string):
    words_list = string.split(' ')
    words_list.reverse()
    return ' '.join(words_list)

if __name__=='__main__':
    string = ' i like this program very much '
    print(reverse_words(string))




