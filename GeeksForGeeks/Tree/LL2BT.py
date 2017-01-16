import queue
from GeeksForGeeks.LinkedList.SinglyLinkedList import LinkedList
"""
Construct Complete Binary Tree from its Linked List Representation

Given Linked List Representation of Complete Binary Tree, construct the Binary tree. A complete binary tree can be
 represented in an array in the following approach.

If root node is stored at index i, its left, and right children are stored at indices 2*i+1, 2*i+2 respectively.
Suppose tree is represented by a linked list in same way, how do we convert this into normal
 linked representation of binary tree where every node has data, left and right pointers?
  In the linked list representation, we cannot directly access the children of the current node unless we
  traverse the list.

"""

class BTNode :
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def ll2bt(head):
    if not head :
        return
    else :
        node = head
        root = BTNode(node.data)
        node = node.next
        que  = queue.Queue()
        que.put(root)

        while node :
            parent = que.get()

            left = BTNode(node.data)
            node = node.next
            que.put(left)

            right  = BTNode(node.data)
            node  = node.next
            que.put(right)

            parent.left = left
            parent.right = right
        return root

def preorder(node):
    if not node :
        return
    else :
        print(node.data)
        preorder(node.left)
        preorder(node.right)

if __name__=='__main__':
    ll = LinkedList()
    for i in range(1,10):
        ll.insert_at_ending(i)
    root = ll2bt(ll.head)
    preorder(root)




