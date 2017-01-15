import sys
from BinaryTree import BinaryTree,BinaryTreeNode

maximum = -1

def build_tree():
    tree = BinaryTree()
    for i in range(1,11):
        tree.add_node(i)
    return tree

def find_max(node):
    if not node:
        return -sys.maxsize
    else :
        return max(find_max(node.get_left()),node.get_data(),find_max(node.get_right()))


def find_maximum(node=None):
    """
    Recursive implementation for finding the maximum element in a tree.
    :param node:
    :return:
    """
    global maximum
    if node is None:
        return maximum
    if node.get_data() > maximum:
        maximum=node.get_data()
    find_maximum(node.get_left())
    find_maximum(node.get_right())
    return maximum

def _find_maximum(node):
    """
    Non-Recursive implementation for finding the maximum element in a tree.
    :param node:
    :return:
    """
    if node is None :
        return
    else:
        max2 = node.data
        queue = []
        queue.append(node)
        while len(queue)!=0 :
            node = queue.pop(0)
            if node.data > max2:
                max2=node.data
            if node.get_left() is not None:
                queue.append(node.get_left())
            if node.get_right() is not None:
                queue.append((node.get_right()))
        return max2


def print_levelorder(root):
    """
    Non-Recursive implementation of Level order
    :param root:
    :return:
    """
    if root is None :
        return
    else :
        queue =[root]
        while len(queue)!=0:
            node = queue.pop(0)
            print(node.data)
            if node.get_left() is not None:
                queue.append(node.get_left())
            if node.get_right() is not None:
                queue.append(node.get_right())



if __name__=="__main__":
    tree = build_tree()
    #tree.level_order()
    print(find_max(tree.root))
    print(__find_max(tree.root))






