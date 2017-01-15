from Trees import BinaryTree



def build_tree():
    tree = BinaryTree()
    for i in range(1,11):
        tree.add_node(i)
    return tree


if __name__=="__main__":
    tree = build_tree()
    print(find_maximum(tree.root))