from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Check if a given Binary Tree is SumTree

Write a function that returns true if the given Binary Tree is SumTree else false.
A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left
subtree and right subtree. An empty tree is SumTree and sum of an empty tree can be considered as 0.
 A leaf node is also considered as SumTree.

Following is an example of SumTree.

          32
        /   \
      10     6
    /    \  /  \
  4      6  3   3

"""

def check_sumtree(node):
    if not node :
        return 0
    else :
        if not node.left and node.right :
            return check_sumtree(node.right)
        elif not node.right and node.left :
            return check_sumtree(node.left)
        elif not node.left and not node.right :
            return node.data
        else  :
            a = check_sumtree(node.left)
            b = check_sumtree(node.right)
            if a > 0 and b > 0 and node.data == a+b :
                return 2*node.data
            else :
                return -1
def check(node):
    return True if check_sumtree(node) > 0 else False


if __name__=='__main__':
    bt  = BinaryTree()
    bt.add_node(32)
    bt.add_node(10)
    bt.add_node(6)
    bt.add_node(4)
    bt.add_node(6)
    bt.add_node(8)
    bt.add_node(3)
    print(check(bt.root))
        