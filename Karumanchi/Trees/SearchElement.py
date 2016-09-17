from BinaryTree import BinaryTree

def build_tree():
    tree = BinaryTree()
    for i in range(1,11):
        tree.add_node(i)
    return tree


def search_element(node,element):
    """
    Recursive implementation for searching for an element
    :param node:
    :param element:
    :return:
    """
    if node is None:
        return False
    if node.data == element:
        return True
    else :
        foo = search_element(node.get_left(),element)
        if foo is True:
            return True
        else :
            return search_element(node.get_right(),element)

def _search_element(root,element):
    """
    Non-Recursive implementation for searching an element
    :param element:
    :return:
    """
    if root is None:
        return False
    else:
        queue = [root]
        while len(queue)!=0:
            node = queue.pop(0)
            if node.get_data() == element:
                return True
            if node.get_left() is not None:
                queue.append(node.get_left())
            if node.get_right() is not None:
                queue.append(node.get_right())
        return False


if __name__ == "__main__":
    tree = build_tree()
    print(search_element(tree.root,5))
    print(search_element(tree.root,15))

    print(_search_element(tree.root,5))
    print(_search_element(tree.root,15))
