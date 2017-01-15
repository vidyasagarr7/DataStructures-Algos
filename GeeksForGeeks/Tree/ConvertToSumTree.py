from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Convert a given tree to its Sum Tree
Given a Binary Tree where each node has positive and negative values. Convert this to a tree where each
node contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are
changed to 0.

For example, the following tree

                  10
               /      \
	     -2        6
           /   \      /  \
	 8     -4    7    5
should be changed to

                 20(4-2+12+6)
               /      \
	   4(8-4)      12(7+5)
           /   \      /  \
	 0      0    0    0

"""

def convert_sumtree(node):
    if not node :
        return 0
    else :
        old_val = node.data
        node.data = convert_sumtree(node.left) + convert_sumtree(node.right)
        return node.data + old_val

def print_preorder(node):
    if not node :
        return
    print(node.data)
    print_preorder(node.left)
    print_preorder(node.right)

if __name__=='__main__':
    bt = BinaryTree()
    bt.add_node(10)
    bt.add_node(-2)
    bt.add_node(6)
    bt.add_node(8)
    bt.add_node(-4)
    bt.add_node(7)
    bt.add_node(5)

    convert_sumtree(bt.root)
    print_preorder(bt.root)






