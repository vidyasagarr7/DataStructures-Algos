from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue
from Karumanchi.Stack import Stack

def print_reverse_llo(root):
    """
    Complete reversing of the order
    :param root:
    :return:
    """
    if not root:
        return None
    else:
        que = Queue.Queue1()
        stack = Stack.Stack()
        que.enqueue(root)
        while not que.is_empty():
            node = que.dequeue()
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())
            stack.push(node)
        while not stack.is_empty():
            print(stack.pop().get_data())


def print_level(node,level):
    if not node:
        return None
    else:
        if level ==1 :
            print(node.get_data())
        elif level>1:
            print_level(node.get_left(),level-1)
            print_level(node.get_right(),level-1)

def find_height(node):
    if not node:
        return 0
    else :
        return max(find_height(node.get_left()),find_height(node.get_right()))+1

def _find_height(root):
    """
    non-recursive implementation
    :param root:
    :return:
    """
    if not root:
        return 0
    else :
        que = Queue.Queue1()
        que.enqueue(root)
        height =0
        left = right = 0
        while not que.is_empty():
            node = que.dequeue()
            if node.get_left():
                que.enqueue(node.get_left())
                left +=1
            if node.get_right():
                que.enqueue(node.get_right())
                right +=1
        height = max(left,right)
        return heigh

def print_reverse_levelorder(root):
    if not root:
        return None
    else:
        height = find_height(root)
        for i in range(height,0,-1):
            print_level(root,i)


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    #print_reverse_levelorder(tree.root)
    #print_level(tree.root,4)
    #print(find_height(tree.root))
    #print_reverse_levelorder(tree.root)
    print(_find_height(tree.root))
