import copy
from GeeksForGeeks.Tree.BinaryTree import BinaryTree,Node


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

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    path = []
    paths = []
    print_paths(bt.root,path,paths)
    path_sum = 8
    ps = []
    for _p in paths :
        if sum(_p) == path_sum :
            ps.append(_p)
    if len(ps) == 0 :
        print('no path sum like such exists')
    else :
        for x in ps : print(x)