from Karumanchi.Queue import Queue

class BinaryTreeNode:
    def __init__(self,data=None):
        self.data=data
        self.left = None
        self.right = None

    def set_data(self,value):
        self.data = value
    def get_data(self):
        return self.data

    def set_left(self,node):
        self.left = node
    def get_left(self):
        return self.left

    def set_right(self,node):
        self.right = node
    def get_right(self):
        return self.right

class BinaryTree:
    def __init__(self,node=None):
        self.root = node

    def add_node(self,value=None):
        new_node = BinaryTreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            que = Queue.Queue1()
            que.enqueue(self.root)
            while not que.is_empty():
                node = que.dequeue()
                if node.get_left() is None:
                    node.set_left(new_node)
                    return
                if node.get_right() is None:
                    node.set_right(new_node)
                    return
                que.enqueue(node.get_left())
                que.enqueue(node.get_right())

    def print_preorder(self,node):
        """
        Recursive implementation of preorder traversal
        :param node:
        :return:
        """
        if not node:
            return None
        else:
            print(node.data)
            self.print_preorder(node.get_left())
            self.print_preorder(node.get_right())

    def _print_preorder(self):
        if not self.root:
            return None
        else:
            stack = []
            stack.append(self.root)
            while len(stack)>0:
                node = stack.pop()
                print(node.data)
                if node.get_right() :
                    stack.append(node.get_right())
                if node.get_left():
                    stack.append((node.get_left()))

    def print_inorder(self,node):
        """
        recursive implementation of inorder traversal
        :param node:
        :return:
        """
        if not node:
            return None
        else:
            self.print_inorder(node.get_left())
            print(node.data)
            self.print_inorder(node.get_right())

    def _print_inorder(self):
        """
        Non-Recursive implementation of Inorder traversal
        :return:
        """
        if not self.root:
            return None
        else:
            stack = []
            node = self.root
            while len(stack) or node:
                if node:
                    stack.append(node)
                    node=node.get_left()
                else:
                    node = stack.pop()
                    print(node.get_data())
                    node=node.get_right()

    def print_postorder(self,node):
        """
        Recursive implementaion of Postorder traversal
        :return:
        """
        if not node:
            return None
        self.print_postorder(node.get_left())
        self.print_postorder(node.get_right())
        print(node.get_data())

    def _print_postorder(self):
        if not self.root:
            return None
        else:
            visited = set()
            stack = []
            node = self.root
            while stack or node :
                if node:
                    stack.append(node)
                    node = node.get_left()
                else :
                    node = stack.pop()
                    if node.get_right() and not node.get_right() in visited:
                        stack.append(node)
                        node=node.get_right()
                    else:
                        visited.add(node)
                        print(node.get_data())
                        node = None

    def print_levelorder(self):
        if not self.root:
            return None
        else:
            que = Queue.Queue1()
            que.enqueue(self.root)
            while not que.is_empty():
                node = que.dequeue()
                if node.get_left():
                    que.enqueue(node.get_left())
                if node.get_right():
                    que.enqueue(node.get_right())
                print(node.data)



if __name__=="__main__":
    btree = BinaryTree()
    for i in range(1,10):
        btree.add_node(i)
    #btree.print_levelorder()
    #btree.print_preorder(btree.root)
    #btree._print_preorder()
    #btree.print_inorder(btree.root)
    #btree._print_inorder()

    #btree.print_postorder(btree.root)
    btree._print_postorder()