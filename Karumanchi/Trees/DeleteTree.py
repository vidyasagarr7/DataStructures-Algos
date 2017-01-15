from BinaryTree import BinaryTree

############ Check this out again #############

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
    node = None

def _delete_tree(root):
    """
    Recursive implementation
    :param root:
    :return:
    """
    if root is None :
        return
    else:
        visited = set()
        stack=[]
        node = root
        if stack or node:
            if node :
                stack.append(node)
                node=node.left
            else :
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    del node

if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)

    delete_tree(tree.root)
    #_delete_tree(tree.root)
    tree.root = None
    tree.level_order()