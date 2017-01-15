from queue import Queue

class Node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree :
    def __init__(self):
        self.root = None

    def add_node(self,item):
        if not self.root :
            self.root = Node(item)
        else :

            que = Queue()
            que.put(self.root)
            new_node = Node(item)
            while not que.empty() :
                node = que.get()

                if not node.left :
                    node.left = new_node
                    return
                if not node.right :
                    node.right = new_node
                    return
                que.put(node.left)
                que.put(node.right)

    def level_order(self):
        if not self.root :
            return
        else :

            que = Queue()
            que.put(self.root)
            while not que.empty() :
                node = que.get()
                print(node.data)
                if node.left :
                    que.put(node.left)
                if node.right :
                    que.put(node.right)

    def preorder(self,node):
        if not node :
            return
        else :
            print(node.data)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_preorder(self):
        if not self.root :
            return
        else :
            stac = [self.root]

            while len(stac) > 0 :
                node = stac.pop()

                print(node.data)
                if node.right :
                    stac.append(node.right)
                if node.left :
                    stac.append(node.left)

    def inorder(self,node):
        if not node :
            return
        else  :
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def print_inorder(self):
        if not self.root :
            return
        else :
            stac = []
            node = self.root

            while node or len(stac) > 0 :
                if node :
                    stac.append(node)
                    node = node.left
                else :
                    node = stac.pop()
                    print(node.data)
                    node = node.right

    def postorder(self,node):
        if not node :
            return
        else :
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def print_postorder(self):
        if not self.root :
            return
        else :
            visited = set()
            node = self.root
            stac = []
            while node or len(stac) > 0 :
                if node :
                    stac.append(node)
                    node = node.left
                else:
                    node = stac.pop()
                    if node.right and node.right not in visited :
                        stac.append(node)
                        node = node.right
                    else :
                        visited.add(node)
                        print(node.data)
                        node = None
    def pprint_postorder(self):
        if not self.root :
            return
        else  :
            stac1 = [self.root]
            stac2 = []

            while len(stac1) > 0 :
                node = stac1.pop()
                stac2.append(node)
                if node.left :
                    stac1.append(node.left)
                if node.right :
                    stac1.append(node.right)

            while len(stac2) >0 :
                node = stac2.pop()
                print(node.data)

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    #bt.level_order()

    #bt.preorder(bt.root)

    #bt.pprint_preorder()

    #bt.inorder(bt.root)

    #bt.print_inorder()

    #bt.postorder(bt.root)

    #bt.print_postorder()

    bt.pprint_postorder()