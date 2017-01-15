from GeeksForGeeks.BST.BST import BST

def find_min(root):
    if not root :
        return
    else :
        node = root
        while node.left :
            node = node.left
        print(node.data)

if __name__=='__main__' :
    bst = BST()
    bst.add_node(5)
    bst.add_node(2)
    bst.add_node(6)
    bst.add_node(1)
    bst.add_node(3)

    find_min(bst.root)