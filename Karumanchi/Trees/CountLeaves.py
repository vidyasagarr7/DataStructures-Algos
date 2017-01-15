from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue

def count_leaves(root):
    if not root:
        return 0
    else:
        que = Queue.Queue1()
        que.enqueue(root)
        count = 0
        while not que.is_empty():
            node = que.dequeue()
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
            if not node.get_left() and not node.get_right():
                count+=1
        return count

def count_full_nodes(root):
    if not root:
        return 0
    else:
        que = Queue.Queue1()
        que.enqueue(root)
        count = 0
        while not que.is_empty():
            node = que.dequeue()
            if node.get_left() and node.get_right():
                count+=1
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
        return count

def count_half_nodes(root):
    if not root :
        return 0
    else:
        que = Queue.Queue1()
        que.enqueue(root)
        count = 0
        while not que.is_empty():
            node = que.dequeue()
            if node.get_right() and not node.get_left() or not node.get_right() and node.get_left():
                count +=1
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
        return count

if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(count_leaves(tree.root))
    print(count_full_nodes(tree.root))
    print(count_half_nodes(tree.root))
