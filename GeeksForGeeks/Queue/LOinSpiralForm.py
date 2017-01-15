from queue import Queue

from Trees.BinaryTree import BinaryTree
from GeeksForGeeks.Queue.LevelOrder import find_height
"""
Level order traversal in spiral form

Write a function to print spiral order traversal of a tree.
For below tree, function should print 1, 2, 3, 4, 5, 6, 7.
"""



def lo_spiral(root):
    if not root :
        return
    else :
        ht = find_height(root)
        ltr = 1
        for i in range(1,ht+1) :
            print_level(root,i,ltr)
            ltr = ltr*-1


def print_level(node,level,sign):
    if not node  :
        return
    if level ==1  :
        print(node.data)
    elif level > 1:
        if sign > 0 :
            print_level(node.left,level-1, sign)
            print_level(node.right,level-1,sign)
        elif sign < 0  :
            print_level(node.right,level-1,sign)
            print_level(node.left,level-1,sign)

def _print_spiral(root):
    '''
    Iterative approach using two stacks , O(n) time algorithm
    :param root:
    :return:
    '''
    if not root :
        return
    else :
        s1,s2 = [root],[]

        while len(s1) or len(s2) :
            while len(s1) :
                node = s1.pop()
                print(node.data)
                if node.left  :
                    s2.append(node.left)
                if node.right :
                    s2.append(node.right)
            while len(s2) :
                node = s2.pop()
                print(node.data)
                if node.right :
                    s1.append(node.right)
                if node.left :
                    s1.append(node.left)




if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,20):
        bt.add_node(i)
    #lo_spiral(bt.root)

    _print_spiral(bt.root)