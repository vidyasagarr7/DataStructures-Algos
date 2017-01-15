from Karumanchi.Trees import BinaryTree
from copy import deepcopy

def root_to_leaf(node,path,value):
    """
    Algorithm to print root to leaf path
    :param root:
    :return:
    """
    if not node:
        return 0
    else:
        if node :
            path.append(node.get_data())
        path_sum = sum(path)
        if path_sum == value:
            print('value found')
        if not node.get_left() and not node.get_right():
            print(path)
            print('sum : ' + str(sum(path)))
        else :
            root_to_leaf(node.get_left(),deepcopy(path),value)
            root_to_leaf(node.get_right(),deepcopy(path),value)


def root_to_leaf_sum(node,path=[]):
    if not node:
        return None
    else :
        if node :
            path.append(node.get_data())

        if not node.get_left() and not node.get_right():
            print(sum(path))
        else :
            root_to_leaf(node.get_left(),deepcopy(path))
            root_to_leaf(node.get_right(),deepcopy(path))


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(root_to_leaf(tree.root,[],8))