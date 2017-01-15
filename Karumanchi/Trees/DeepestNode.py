import queue
from BinaryTree import BinaryTree

def deepest_node(root):
    if root is None:
        return
    else:
        que = queue.Queue()
        que.put(root)
        node = None
        while not que.empty():
            node = que.get()
            if node.get_left():
                que.put(node.get_left())
            if node.get_right():
                que.put(node.get_right())
        return node.data

### REVISIT THIS #######

def delete_node(root):
    if root is None:
        return
    else:
        que=queue.Queue()
        que.put(root)
        if not que.empty():
            node = que.get()
            if node.get_left():
                que.put(node.get_left())
            if node.get_right():
                que.put(node.get_right())
        root.data,node.data=node.data,root.data
        del node


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)

    print(deepest_node(tree.root))
    delete_node(tree.root)
    tree.level_order()