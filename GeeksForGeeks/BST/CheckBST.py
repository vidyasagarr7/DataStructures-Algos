from GeeksForGeeks.BST.BST import BST
from GeeksForGeeks.Tree.BinaryTree import BinaryTree


# wrong code.   
def check_bst(node):
    if not node :
        return True
    else :
        if node.left and node.left.data > node.data :
            return False
        if node.right and node.right.data < node.data  :
            return False
        if node.left and not node.right and node.left.data < node.data :
            return check_bst(node.left)
        if node.right and not node.left and node.right.data > node.data :
            return check_bst(node.right)
        if node.left and node.right and node.data > node.left.data and node.data < node.right.data :
            return check_bst(node.left) and check_bst(node.right)

if __name__=='__main__':
    bst = BST()
    bst.add_node(5)
    bst.add_node(2)
    bst.add_node(6)
    bst.add_node(1)
    bst.add_node(3)


    print(check_bst(bst.root))

    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    print(check_bst(bt.root))