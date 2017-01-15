import sys
from GeeksForGeeks.Tree.BinaryTree import Node,BinaryTree


def find_maxwidth(node,count,level):
    if not node :
        return
    else :
        if level in count :
            count[level] += 1
        else :
            count[level] = 1
        find_maxwidth(node.left,count,level+1)
        find_maxwidth(node.right,count,level+1)

def max_width(node):
    count = {}
    level = 0
    find_maxwidth(node,count,level)
    maxw = -sys.maxsize
    for key,value in count.items() :
        if value > maxw :
            maxw = value
    return maxw

if __name__=='__main__':    
    bt = BinaryTree()
    for i in range(1,20):
        bt.add_node(i)
    print(max_width(bt.root))