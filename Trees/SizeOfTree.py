from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue

def size_of_tree(node):
    """
    recursive implementation for fiding the size of tree
    :param node:
    :return:
    """
    if not node:
        return 0
    else :
        return size_of_tree(node.get_left())+size_of_tree(node.get_right())+1

def _size_of_tree(root):
    if not root:
        return 0
    else:
        size = 0
        que = Queue.Queue1()
        que.enqueue(root)
        while not que.is_empty():
            node = que.dequeue()
            size+=1
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
        return size

if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(size_of_tree(tree.root))
    print(_size_of_tree(tree.root))