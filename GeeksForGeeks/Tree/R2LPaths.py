import copy
from GeeksForGeeks.Tree.BinaryTree import BinaryTree,Node

"""
Given a binary tree, print out all of its root-to-leaf paths one per line.

"""
def print_paths(node,path,paths):
    if not node :
        return
    else :
        path.append(node.data)
        if node.left is None and node.right is None:
            paths.append(copy.deepcopy(path))
        if node.left :
            print_paths(node.left,path,paths)
            path.pop()
        if node.right :
            print_paths(node.right,path,paths)
            path.pop()


def _ppaths(node,path,paths):
    if not node :
        return
    else :
        path.append(node.data)
        if not node.left and not node.right :
            paths.append(copy.deepcopy(path))
        if node.left:
            _ppaths(node.left,path,paths)
            path.pop()
        if node.right :
            _ppaths(node.right,path,paths)
            path.pop()



if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    path = []
    paths = []
    print_paths(bt.root,path,paths)
    print(paths)

    p = []
    ps = []
    _ppaths(bt.root,p,ps)
    print(ps)