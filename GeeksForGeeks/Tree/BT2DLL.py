from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Convert a given Binary Tree to Doubly Linked List | Set 2

Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL).
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of
Inorder traversal (left most node in BT) must be head node of the DLL.

"""

def convert(root):
    if not root :
        return
    else :
        node = bt2dll(root)
        while node.left :
            node = node.left
        return node
def bt2dll(node):
    if not node :
        return
    else :

        if node.left :
            left = bt2dll(node.left)
            while left.right :
                left = left.right
            left.right = node
            node.left = left

        if node.right  :
            right = bt2dll(node.right)
            while right.left :
                right  = right.left
            right.left = node
            node.right = right
        return  node

def printll(head):
    if not head :
        return
    else :
        current = head
        while current:
            print(current.data)
            current = current.right

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    root = convert(bt.root)
    printll(root)
