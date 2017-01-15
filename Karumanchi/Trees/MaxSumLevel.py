import sys
from Karumanchi.Queue import Queue
from Karumanchi.Trees import BinaryTree


def find_height(root):
    if not root:
        return 0
    else:
        return max(find_height(root.get_left()),find_height(root.get_right()))+1

def level_sum(root,level):
    if not root:
        return 0
    else :
        que = Queue.Queue1()
        que.enqueue([root,1])
        summ = 0
        while not que.is_empty():
            node,depth = que.dequeue()
            if depth ==level:
                summ+= node.get_data()
            if node.get_left():
                que.enqueue([node.get_left(),depth+1])
            if node.get_right():
                que.enqueue([node.get_right(),depth+1])
        return summ


def max_sum_in_level(root):
    if not root:
        return 0
    else :
        height=find_height(root)
        max_sum = -sys.maxsize
        for i in range(height,0,-1):
            max_sum = max(level_sum(root,i),max_sum)
        return max_sum

# revisit this to optimise
def _max_level_sum(root):
    if not root:
        return 0



if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(max_sum_in_level(tree.root))