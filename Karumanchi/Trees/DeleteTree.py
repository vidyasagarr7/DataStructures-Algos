from BinaryTree import BinaryTree

def delete_tree(node):
    """
    Delete a tree - Post order - Recursive Implementation
    :param root:
    :return:
    """
    if node is None:
        return
    delete_tree(node.right)
    delete_tree(node.left)
    print("deleting the node" + str(node.data))
    del node

def _delete_tree(root):
    """
    Non-Recursive implementation
    :param root:
    :return:
    """
    if root is None:
        return
    else:



if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    tree.level_order()

    delete_tree(tree.root)
