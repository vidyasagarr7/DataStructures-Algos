from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Check for Children Sum Property in a Binary Tree

Given a binary tree, write a function that returns true if the tree satisfies below property.

For every node, data value must be equal to sum of data values in left and right children.

Consider data value as 0 for NULL children. Below tree is an example


"""

def check_children_sum(node):
    if not node or (not node.left and not node.right) :
        return True
    else :
        l_val = r_val = 0
        if node.left :
            l_val = node.left.data
        if node.right:
            r_val = node.right.data
        if (l_val+r_val == node.data) and check_children_sum(node.left) and check_children_sum(node.right) :
            return True
        else :
            return False

if __name__=='__main__':
    bt = BinaryTree()
    bt.add_node(10)
    bt.add_node(8)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(5)
    bt.add_node(2)
    #bt.print_levelorder()

    print(check_children_sum(bt.root))

    bt2 = BinaryTree()
    for i in range(1,10):
        bt2.add_node(i)
    print(check_children_sum(bt2.root))
