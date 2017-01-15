from GeeksForGeeks.Tree.BinaryTree import BinaryTree
import copy


def r2l(node,path,paths):
    if not node :
        return
    else :
        path.append(node.data)

        if not node.right and not node.left :
            paths.append(copy.deepcopy(path))

        if node.left :
            r2l(node.left,path,paths)
            path.pop()

        if node.right :
            r2l(node.right,path,paths)
            path.pop()
        return paths




if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    path = []
    paths = []
    r2l(bt.root,path,paths)
    print(paths)

