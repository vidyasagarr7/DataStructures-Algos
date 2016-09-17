import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data

    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

class BinaryTree:
    def __init__(self,value=None):
        self.root=value

    def add_node(self,value):
        new_node = BinaryTreeNode(value)

        if self.root is None:
            self.root=new_node
        else:
            que = queue.Queue()
            que.put(self.root)
            while not que.empty():
                    node = que.get()
                    if node.left is None:
                        node.left = new_node
                        return
                    if node.right is None :
                        node.right = new_node
                        return
                    que.put(node.left)
                    que.put(node.right)

    def print_preorder(self):
        """
        Non-Recursive implementation of PreOrder Traversal
        :return:
        """
        if self.root is None:
            return
        else:
            stack = [self.root]
            while len(stack) != 0:
                node = stack.pop()
                print(node.get_data())
                if node.get_right() is not None:
                    stack.append(node.get_right())
                if node.get_left() is not None:
                    stack.append(node.get_left())

    def _print_preorder(self,node):
        """
        Recursive implementation of Pre-Order Traversal
        :param node:
        :return:
        """
        if node is None:
            return
        print(node.data)
        self.print_preorder(node.left)
        self.print_preorder(node.right)



    def _print_inorder(self,node):
        """
        Recursive implementation of In-Order Traversal
        :return:
        """
        if node is None:
            return
        self._print_postorder(node.get_left())
        print(node.get_data())
        self._print_postorder(node.get_right())

    def print_inorder(self):
        """
        Non-Recursive implementation of In-Order Traversal
        :return:
        """
        if self.root is None :
            return
        else :
            stack = []
            node = self.root
            while len(stack) or node:
                if node is not None:
                    stack.append(node)
                    node = node.get_left()
                else:
                    node =stack.pop()
                    print(node.data)
                    node=node.get_right()

    def _print_postorder(self,node):
        """
        Recursive implemenataion of Post Order
        :return:
        """
        if node is None:
            return
        else :
            self._print_postorder(node.get_left())
            self._print_postorder(node.get_right())
            print(node.data)

    def print_postorder(self):
        """
        Recursive implementation of Post-Order
        :return:
        """
        if self.root is None :
            return
        else:
            visited = set()
            stack =[]
            node = self.root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.get_left()
                else:
                    node = stack.pop()
                    if node.right and not node.right in visited:
                        stack.append(node)
                        node=node.get_right()
                    else :
                        visited.add(node)
                        print(node.get_data())
                        node = None

    def level_order(self):
        """
        Non-Recursive implementation of Level Traversal
        :param node:
        :return:
        """
        if self.root is None:
            return
        else :
            que = queue.Queue()
            que.put(self.root)
            while not que.empty():
                node = que.get()
                print(node.get_data())
                if node.left is not None:
                    que.put(node.get_left())
                if node.right is not None:
                    que.put(node.get_right())

    def size_tree(self):
        """
        Algorithm to find the size of the tree.
        :return:
        """
        count = 0
        if self.root is None:
            return count
        else :

            que = queue.Queue()
            que.put(self.root)
            while not que.empty():
                node = que.get()
                count+=1
                if node.left is not None :
                    que.put(node.get_left())
                if node.right is not None:
                    que.put(node.get_right())

            return count
    def _size_tree(self,node):
        """
        Recursive implementation of binary tree for finding the number of elements in the tree
        :return:
        """
        if node is None:
            return 0
        else :
            return self._size_tree(node.get_left()) + self._size_tree(node.get_right()) +1

    def _height(self,node):
        """

        :return:
        """
        if node == None:
            return 0
        return max(self._height(node.left),self._height(node.right))+1
    #### test ###
    def height(self):
        """
        Non-recursive Implementation
        :return:
        """
        if self.root is None:
            return 0
        else:
            que = queue.Queue()
            que.put([self.root,1])
            depth = 0
            while not que.empty():
                node,depth = que.get()
                if node.get_left() :
                    que.put([node.get_left(),depth+1])
                if node.get_right():
                    que.put([node.get_right(),depth+1])
            return depth

    def number_of_leaves(self):
        """
        Non-Recursive implementation for finding number of leaves in a tree
        :return:
        """
        if self.root is None:
            return 0
        else:
            que = queue.Queue()
            que.put(self.root)
            count=0
            while not que.empty():
                node = que.get()
                if node.get_left() is None and node.get_right() is None:
                    count+=1
                if node.get_left():
                    que.put(node.get_left())
                if node.get_right():
                    que.put(node.get_right())

            return count

    def number_of_fullnodes(self):
        """

        :return: number of full nodes in a tree
        """
        if not self.root :
            return 0
        else:
            que= queue.Queue()
            que.put(self.root)
            count = 0
            while not que.empty():
                node = que.get()
                if node.get_left() and node.get_right():
                    count+=1
                if node.get_left():
                    que.put(node.get_left())
                if node.get_right():
                    que.put(node.get_right())
            return count

    ########## have to test this code ##########

    def number_of_halfnodes(self):
        """

        :return: number of half nodes
        """
        if not self.root:
            return 0
        else:
            que = queue.Queue()
            que.put(self.root)
            count = 0
            while not que.empty():
                node = que.get()
                if (node.get_left() and not node.get_right()) or (not node.get_left() and node.get_right()):
                    count+=1
                if node.get_left():
                    que.put(node.get_left())
                if node.get_right():
                    que.put(node.get_right())
            return count

    def diameter(self,node):
        """

        :return: diameter of the tree
        """
        if node is None:
            return 0
        else :
            left_height= self.height(node.left)
            right_height = self.height(node.right)

            left_diameter = self.diameter(node.left)
            right_diameter = self.diameter(node.right)

            return max(left_height+right_height+1,max(left_diameter+right_diameter))


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    print(tree.level_order())

    print("Size of Tree : "+str(tree.size_tree()))

    print("height of tree : "+ str(tree.height()))

    print("number of leaves : "+ str(tree.number_of_leaves()))

    print("number of full nodes :  "+ str(tree.number_of_fullnodes()))

    print("number of half nodes: "+ str(tree.number_of_halfnodes()))
