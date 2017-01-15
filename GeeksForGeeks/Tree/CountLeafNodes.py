import queue
from GeeksForGeeks.Tree.BinaryTree import Node,BinaryTree

def count_leaf_nodes(root):
    count = 0
    if not root :
        return count
    else  :
        que = queue.Queue()
        que.put(root)
        while not que.empty() :
            node = que.get()
            if node.left :
                que.put(node.left)
            if node.right :
                que.put(node.right)
            if not node.left and not node.right :
                count +=1
        return count

def leaf_count(node):
    if not node :
        return 0
    if not node.left and not node.right :
        return 1
    else :
        return leaf_count(node.left) + leaf_count(node.right)

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    print(count_leaf_nodes(bt.root))
    print(leaf_count(bt.root))