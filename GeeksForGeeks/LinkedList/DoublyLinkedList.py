
class Node :
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add_node(self,value):
        if not self.head :
            self.head = Node(value)
            self.last = self.head
            self.last.prev = self.head
        else :
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_node_end(self,value):
        if not self.head :
            self.head= Node(value)
            self.last = self.head
        else :
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def print_list(self):
        if not self.head :
            return
        else :
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def delete_node(self,node):
        if not node :
            return
        else :
            if not self.head :
                return
            if self.head == node :
                self.head = node.next

            if node.next :
                node.next.prev = node.prev

            if node.prev :
                node.prev.next = node.next

    def delete(self,value):
        if not value :
            return
        else :
            if not self.head :
                return
            if self.head.data == value :
                self.head = self.head.next

            current = self.head
            while current :
                if current.data == value :
                    break
                else :
                    current = current.next
            current.prev.next = current.next

    def reverse(self):
        if not self.head :
            return
        else :
            current = self.head
            prev = None

            while current :
                next = current.next
                current.next = prev
                current.prev = next
                prev = current
                current = next
            self.head = prev


if __name__=='__main__':
    dll = DoublyLinkedList()
    for i in range(1,10):
        #dll.add_node(i)
        dll.add_node_end(i)

    #dll.print_list()
    dll.delete(5)
    dll.print_list()

    #print(dll.last.data)