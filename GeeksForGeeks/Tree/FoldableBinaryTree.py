from GeeksForGeeks.Tree.BinaryTree import BinaryTree
from GeeksForGeeks.Tree.Convert2Mirror import create_mirror

"""
Foldable Binary Trees

Question: Given a binary tree, find out if the tree can be folded or not.

A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other.
 An empty tree is considered as foldable.

"""

def check_identical_structure(left,right):
    if  left is None and right is None :
        return True
    if ( left and  right ) and ( check_identical_structure(left.left,right.left)
        and check_identical_structure(left.right,right.right)) :
        return True
    return False

def check_foldable(node):
    if not node :
        return True
    else :
        create_mirror(node.left)
        result = check_identical_structure(node.left,node.right)
        create_mirror(node.left)
        return result

if __name__=='__main__':
    ll = BinaryTree()
    ll.add_node(10)
    ll.add_node(7)
    ll.add_node(15)
    ll.add_node(None)
    ll.add_node(9)
    ll.add_node(11)
    ll.add_node(None)
    print(check_foldable(ll.root))

    ll2 = BinaryTree()
    ll2.add_node(10)
    ll2.add_node(7)
    ll2.add_node(15)
    ll2.add_node(9)
    ll2.add_node(None)
    ll2.add_node(None)
    #ll2.add_node(11)
    print(check_foldable(ll2.root))

    # ll2.print_levelorder()































