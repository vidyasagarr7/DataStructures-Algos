from GeeksForGeeks.Tree.BinaryTree import Node,BinaryTree

"""

Level order traversal - functions for printing elements in a level and prints all the elements in level order

"""


def print_level(node,level,itr):
    if not node :
        return
    if level == 1 :
        print(node.data)
    else :
        if not itr :
            print_level(node.left,level-1,itr)
            print_level(node.right,level-1,itr)
        else :
            print_level(node.right,level-1,itr)
            print_level(node.left,level-1,itr)

def level_order(root,ht,spiral):
    flag = False if spiral else True
    for i in range(1,ht+1):
        print_level(root,i,flag)
        flag = not flag if spiral else flag

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,20):
        bt.add_node(i)
    ht = bt._height(bt.root)
    level_order(bt.root,ht,True)
    #print_level(bt.root,4)
