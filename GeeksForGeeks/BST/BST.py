import queue
"""
Binary Search Tree implementation

"""

class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST  :
    def __init__(self):
        self.root = None

    def add_node(self,value ):
        if not self.root :
            self.root = Node(value)
        else:
            new_node = Node(value)
            que = queue.Queue()
            que.put(self.root)

            while not que.empty():
                node = que.get()

                if not node.left and value < node.data :
                    node.left = new_node
                    return
                if not node.right and value > node.data :
                    node.right = new_node
                    return
                if node.left :
                    que.put(node.left)
                if node.right :
                    que.put(node.right)

    def _add_node(self,value):
        if not self.root :
            self.root = Node(value)
        else :
            current = self.root
            new_node = Node(value)
            while True :
                if value <= current.data :
                    if current.left  :
                        current = current.left
                    else :
                        current.left = new_node
                        break
                else:
                    if current.right :
                        current = current.right
                    else :
                        current.right = new_node
                        break

        return

    def print_levelorder(self):
        if not self.root:
            return
        else:
            que = queue.Queue()
            que.put(self.root)
            while not que.empty():
                node = que.get()
                print(node.data)
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)

    def print_preorder(self):
        """
        Non - recursive implementation of preorder traversal
        :return:
        """
        if not self.root:
            return
        else:
            stac = [self.root]
            while len(stac) != 0:
                node = stac.pop()
                print(node.data)
                if node.right:
                    stac.append(node.right)
                if node.left:
                    stac.append(node.left)

    def _print_preorder(self, node):
        if not node:
            return
        print(node.data)
        self._print_preorder(node.left)
        self._print_preorder(node.right)

    def print_inorder(self):
        """
        iterative implemetation of inorder traversal
        :return:
        """
        if not self.root:
            return
        else:
            node = self.root
            stack = []
            while node or len(stack) != 0:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    print(node.data)
                    node = node.right

    def _print_inorder(self, node):
        """
        Recursive implementation of indorder traversal
        :param node:
        :return:
        """
        if not node:
            return
        self._print_inorder(node.left)
        print(node.data)
        self._print_inorder(node.right)

    def print_postorder(self):
        """
        Iterative implementation of postorder traversal
        :return:
        """

        if not self.root:
            return
        else:
            visited = {}
            node = self.root
            stack = []

            while node or len(stack) != 0:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if node.right not in visited and node.right:
                        stack.append(node)
                        node = node.right
                    else:
                        print(node.data)
                        visited[node] = node
                        node = None

    def _print_postorder(self, node):
        """
        Recursive implementation of Postorder traversal
        :param node:
        :return:
        """
        if not node:
            return
        self._print_postorder(node.left)
        self._print_postorder(node.right)
        print(node.data)

    def calculate_size(self):
        """
        Iterative implementation
        :return:
        """
        if not self.root:
            return 0
        else:
            count = 0
            que = queue.Queue()
            que.put(self.root)
            while not que.empty():
                node = que.get()
                count += 1
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            return count

    def size(self, node):
        """
        recursive implementation for size of tree.
        :param node:
        :return:
        """
        if not node:
            return 0
        return self.size(node.left) + self.size(node.right) + 1

    def _height(self, node):
        """
        recursive implementation for finding the height of the tree.
        :param node:
        :return:
        """
        if not node:
            return 0
        else:
            return max(self._height(node.left), self._height(node.right)) + 1

    def delete_tree(self, node):
        """
        recursive implemenation of Postorder traversal
        :param node:
        :return:
        """
        if not node:
            return
        self.delete_tree(node.left)
        self.delete_tree(node.right)
        node = None

    def diameter(self, node):
        """
        recursive implementation
        :param node:
        :return:
        """
        if not node:
            return 0
        else:
            lheight = self._height(node.left)
            rheight = self._height(node.right)

            ldia = self.diameter(node.left)
            rdia = self.diameter(node.right)

            return max(ldia, rdia, 1 + lheight + rheight)

    def _diameter(self, node):
        if not node:
            return 0, 0
        else:
            ldia, lh = self._diameter(node.left)
            rdia, rh = self._diameter(node.right)

            ht = 1 + max(lh, rh)
            dia = max(ldia, rdia, 1 + lh + rh)

            return dia, ht

if __name__=='__main__':
    bst = BST()
    bst._add_node(5)

    for i in range(1,5):
        bst._add_node(i)
    for j in range(6,10):
        bst._add_node(j)

    bst.print_levelorder()

