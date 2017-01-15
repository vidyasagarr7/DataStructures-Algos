from Karumanchi.Trees import BinaryTree

def print_ancestors(root,node):
    if not root:
        return False
    elif root.get_data() == node or root.get_left() == node or root.get_right()==node or print_ancestors(root.get_left(),node) \
        or print_ancestors(root.get_right(),node):
        print(root.get_data())
        return True
    return False

if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print_ancestors(tree.root,5)