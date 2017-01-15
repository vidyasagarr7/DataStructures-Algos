from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Boundary Traversal of binary tree

Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
 For example, boundary traversal of the following tree is “20 8 4 10 14 25 22”


"""

def print_leftboundary(node):
    if not node :
        return
    else :
        if node.left :
            print(node.data)
            print_leftboundary(node.left)
        elif node.right :
            print(node.data)
            print_leftboundary(node.right)

def print_rightboundary(node):
    if not node :
        return
    else :
        if node.right :
            print_rightboundary(node.right)
            print(node.data)
        elif node.left :
            print_rightboundary(node.left)
            print(node.data)

def print_leafnodes(node):
    if not node :
        return
    else :
        print_leafnodes(node.left)
        if not node.left and not node.right :
            print(node.data)
        print_leafnodes(node.right)

def boundary_traversal(root):
    if not root :
        return
    else :
        print(root.data)
        print_leftboundary(root.left)
        print_leafnodes(root.left)
        print_leafnodes(root.right)
        print_rightboundary(root.right)

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    boundary_traversal(bt.root)