from GeeksForGeeks.LinkedList.SinglyLinkedList import  LinkedList,Node

"""
Write a function to get Nth node in a Linked List
Write a GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position.

Example:

Input:  1->10->30->14,  index = 2
Output: 30
The node at index 2 is 30


"""

def getNthNode(head,n):
    """
    function to return nth node from the start in a singly linkedlist
    :param head:
    :param n: nth node
    :return:
    """
    if not head :
        return None
    count = 0
    temp = head
    while temp and count < n:
        temp = temp.next
        count += 1
    if temp :
        return temp.data
    else :
        return temp



if __name__=="__main__":
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_begining(i)
    print(getNthNode(ll.head,5))
xt
