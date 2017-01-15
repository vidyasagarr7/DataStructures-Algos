from GeeksForGeeks.Tree.BinaryTree import BinaryTree
"""

Convert an arbitrary Binary Tree to a tree that holds Children Sum Property
Question: Given an arbitrary binary tree, convert it to a binary tree that holds Children Sum Property.
You can only increment data values in any node (You cannot change structure of tree and cannot decrement
 value of any node).

For example, the below tree doesn’t hold the children sum property, convert it to a tree that holds the property.

             50
           /     \
         /         \
       7             2
     / \             /\
   /     \          /   \
  3        5      1      30
Algorithm:

"""

def convert(node):
    if not node :
        return
    else :
        ldata = 0
        rdata = 0
        diff = 0
        convert(node.left)
        convert(node.right)
        if node.left :
            ldata = node.left.data
        if node.right :
            rdata = node.right.data

        diff = ldata + rdata - node.data
        if diff > 0 :
            node.data = node.data + diff
        elif diff < 0 :
            increment(node.left,-diff)

def increment(node,diff):
    if not node :
        return
    else :
        node.data = node.data + diff
        if node.left :
            increment(node.left,diff)
        elif node.right :
            increment(node.right,diff)

if __name__=='__main__':
    bt = BinaryTree()
    bt.add_node(50)
    bt.add_node(7)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(5)
    bt.add_node(1)
    bt.add_node(30)

    convert(bt.root)
    bt.print_levelorder()

