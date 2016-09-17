import queue
from BinaryTree import BinaryTree

def height(root):
    if not root:
        return 0
    else:
        que = queue.Queue()
        que.put([root,1])
        depth = 0
        while not que.empty():
            node,depth = que.get()
            if node.left:
                que.put([node.left,depth+1])
            if node.right:
                que.put([node.right,depth+1])
        return depth

def diameter(root):
    if root is None :
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left_height + right_height + 1,max(left_diameter,right_diameter))


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(height(tree.root))
    print(diameter(tree.root))
