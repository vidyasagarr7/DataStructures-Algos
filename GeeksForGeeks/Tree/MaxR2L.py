import copy
from GeeksForGeeks.Tree.BinaryTree import BinaryTree,Node

"""
Find the maximum sum leaf to root path in a Binary Tree
Given a Binary Tree, find the maximum sum path from a leaf to root. For example, in the following tree,
there are three leaf to root paths 8->-2->10, -4->-2->10 and 7->10. The sums of these three paths are 16, 4 and 17
respectively. The maximum of them is 17 and the path for maximum is 7->10.

                  10
               /      \
	     -2        7
           /   \
	 8     -4
"""


def find_max_sum(node,path,paths):
    if not node :
        return
    else :
        path.append(node.data)
        if not node.left and not node.right :
            paths.append(copy.deepcopy(path))
        if node.left :
            find_max_sum(node.left,path,paths)
            path.pop()
        if node.right :
            find_max_sum(node.right,path,paths)
            path.pop()



if __name__=='__main__':

    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    path = []
    paths = []
    find_max_sum(bt.root,path,paths)
    current_sum = 0
    target = []

    for _ in paths :
        _sum = sum(_)
        if _sum > current_sum :
            target = _
            current_sum = _sum

    print(target)

