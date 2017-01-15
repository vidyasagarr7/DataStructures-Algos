import queue

class Node  :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree  :
    def __init__(self):
        self.root = None

    def add_node(self,value):
        if not self.root :
            self.root = Node(value)
        else :
            new_node = Node(value)
            current = self.root
            while True :

                if value <= current.data :
                    if current.left :
                        current = current.left
                    else :
                        current.left = new_node
                        break
                else :
                    if current.right :
                        current = current.right
                    else :
                        current.right = new_node
                        break
            return

    def print_levelorder(self):
        if not self.root :
            return
        else :
            que = queue.Queue()
            que.put(self.root)

            while not que.empty() :
                node = que.get()
                print(node.data)
                if node.left :
                    que.put(node.left)
                if node.right :
                    que.put(node.right)

    def search(self,node,value):
        if not node :
            return False
        else :
            if node.data ==value :
                return True
            elif value < node.data :
                return self.search(node.left,value)
            else :
                return self.search(node.right,value)

if __name__=='__main__':
    bst = BinarySearchTree()
    bst.add_node(5)
    for i in range(1,5):
        bst.add_node(i)
    for i in range(6,10):
        bst.add_node(i)
    bst.print_levelorder()

    print(bst.search(bst.root,1))

    print(bst.search(bst.root,8))
    print(bst.search(bst.root,15))






