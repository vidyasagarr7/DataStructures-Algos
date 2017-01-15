"""
Print list items containing all characters of a given word

There is a list of items. Given a specific word, e.g., “sun”,
print out all the items in list which contain all the characters of “sun”.

For example if the given word is “sun” and the items are “sunday”, “geeksforgeeks”, “utensils”, “”just” and “sss”,
then the program should print “sunday” and “utensils”.

"""

def print_list_items(list_items,string):
    NO_CHARS = 256
    hash_table = [0]*NO_CHARS

    for item in list_items :
        count = 0
        for ch in string:
            hash_table[ord(ch)] += 1
        for ch in item :
            if hash_table[ord(ch)] > 0:
                count +=1
                hash_table[ord(ch)] -= 1
        if count == len(string) :
            print(item)
    return

if __name__=='__main__':
    list_items = ['sunday','utensilsu','justnu','sss','geeksforgeeks']
    print_list_items(list_items,'suun')