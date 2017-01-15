from GeeksForGeeks.LinkedList.DoublyLinkedList import DoublyLinkedList

"""
Find the first non-repeating character from a stream of characters

Given a stream of characters, find the first non-repeating character from stream.
You need to tell the first non-repeating character in O(1) time at any moment.
"""

NO_CHARS = 256
def first_nonrepeating_char(input_list):
    if not input_list :
        return
    else :
        dll = DoublyLinkedList()
        visited = [0]*NO_CHARS
        in_dll = [0]*NO_CHARS
        for char in input_list :
            if visited[ord(char)] == 0:
                if in_dll[ord(char)] == 0 :
                    dll.add_node_end(char)
                    in_dll[ord(char)] = 1
                elif in_dll[ord(char)] == 1:
                    dll.delete(char)
                    visited[ord(char)] = 1
            else :
                pass
        return dll.head.data

if __name__=='__main__':
    string = 'geeksforgeeksandgeeksquizfor'
    print(first_nonrepeating_char(list(string)))


