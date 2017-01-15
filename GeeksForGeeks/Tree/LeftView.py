from GeeksForGeeks.Tree.BinaryTree import BinaryTree
import queue

"""
Print Left View of a Binary Tree

Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree
is visited from left side. Left view of following tree is 12, 10, 25.

          12
       /     \
     10       30
            /    \
          25      40

"""

def print_leftview(root):

    if not root :
        return
    else :

        que = queue.Queue()
        que.put((root,1))
        prev_level = 0

        while not que.empty() :
            node,level = que.get()

            if level - prev_level == 1 :
                prev_level = level
                print(node.data)

            if node.left :
                que.put((node.left,level+1))
            if node.right :
                que.put((node.right,level+1))


def leftview(node,level,prev_level) :
    if not node :
        return
    else :
        if prev_level[0] < level :
            prev_level[0] = level
            print(node.data)
        leftview(node.left,level+1,prev_level)
        leftview(node.right,level+1,prev_level)



if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    print_leftview(bt.root)
    prev_level = [0]
    leftview(bt.root,1,prev_level)









