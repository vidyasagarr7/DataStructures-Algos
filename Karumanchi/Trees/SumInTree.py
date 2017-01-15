from Trees import BinaryTree
from Karumanchi.Queue import Queue

def find_sum(node):
    if not node :
        return 0
    else:
        return node.get_data() + find_sum(node.get_left())+ find_sum(node.get_right())

def _find_sum(node):
    if not node:
        return 0
    else:
        total_sum = 0
        que = Queue.Queue1()
        que.enqueue(node)
        while not que.is_empty():
            temp = que.dequeue()
            total_sum += temp.get_data()
            if temp.get_left():
                que.enqueue(temp.get_left())
            if temp.get_right():
                que.enqueue(temp.get_right())
        return total_sum

if __name__=="__main__":
    tree = BinaryTree.BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(_find_sum(tree.root))