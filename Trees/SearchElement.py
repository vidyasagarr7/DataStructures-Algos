from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue

def search_element(node,element):
    """
    Algorithm for searching an element Recursively
    :param node:
    :param element:
    :return:
    """
    if not node:
        return False
    else:
        if node.data == element:
            return True
        return search_element(node.get_left(),element) or search_element(node.get_right(),element)

def _search_element(root,element):
    """
    Non-Recursive implementation for searching an element in binary Tree
    :param root:
    :param element:
    :return:
    """
    if not root :
        return False
    else:
        que = Queue.Queue1()
        que.enqueue(root)
        while not que.is_empty():
            node = que.dequeue()
            if node.data == element:
                return True
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
        return False


if __name__=="__main__":
    tree= BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    for i in range(1,15):
        print(_search_element(tree.root,i))

