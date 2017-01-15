import queue
from GeeksForGeeks.Tree.BinaryTree import BinaryTree
"""
Get Level of a node in a Binary Tree

Given a Binary Tree and a key, write a function that returns level of the key.

For example, consider the following tree. If the input key is 3, then your function should return 1.
If the input key is 4, then your function should return 3. And for key which is not present in key,
then your function should return 0.
"""


def get_level(root,value):
    if not root :
        return
    else :

        que = queue.Queue()
        que.put((root,1))
        while not que.empty() :
            node,level = que.get()
            if node.data == value  :
                return level
            if node.left :
                que.put((node.left,level+1))
            if node.right :
                que.put((node.right,level+1))

def getlevel(node,target,level):
    if not node :
        return -1
    else :
        if node.data == target :
            return level
        else :
            a = getlevel(node.left,target,level+1)
            b = getlevel(node.right,target,level+1)

            return a if a != -1 and b == -1 else b


if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    print(get_level(bt.root,8))

    print(getlevel(bt.root,8,1))