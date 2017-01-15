import sys
from Trees.BinaryTree import BinaryTree
from Karumanchi.Queue import Queue

def find_max(node):
    """
    Recursive implementation for finding the maximum element in the tree
    :param node:
    :return:
    """
    if not node:
        return -sys.maxsize
    else:
        return max(find_max(node.get_left()),node.get_data(),find_max(node.get_right()))

def _find_max(root):
    """
    Non-Recursive implementation for finding the maximum element in the tree
    :return:
    """
    maximum = -sys.maxsize
    if not root:
        return None
    else:
        que = Queue.Queue1()
        que.enqueue(root)
        while not que.is_empty():
            node = que.dequeue()
            if node.data > maximum :
                maximum=node.data
            if node.get_left() :
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
    return maximum

if __name__=="__main__":
    btree = BinaryTree()
    for i in range(1,10):
        btree.add_node(i)
    #print(find_max(btree.root))
    print(_find_max(btree.root))