# didnt implement completely. -- Revisit this


class DoubleLinkedListNode:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None

    def set_data(self,value):
        self.data = value
    def get_data(self):
        return self.data

    def set_prev(self,node):
        self.prev = node
    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    def set_next(self,node):
        self.next = node
    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None




class DoublyLinkedList:

    def __init__(self,head=None):
        self.head = head
        self.length = 0

    def insert_at_beginning(self,value):
        new_node = DoubleLinkedListNode(value)
        if not self.head:
            self.head = new_node
        else :
            next_node = self.head
            next_node.prev = new_node
            self.head = new_node
            self.head.next = next_node
        self.length += 1

    def insert_at_ending(self,value):
        new_node = DoubleLinkedListNode(value)
        if not self.head :
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length +=1

    def insert_at_postition(self,position):
        if self.length < position:
            return "enter a valid position"
        if not self.head :
            return "linked list is empty"
        else:
            count = 0
            current = self.head
            while count < position:
                current = current



    def print_ll(self):
        if not self.head:
            return
        else :
            current = self.head
            while current:
                print(current.data)
                current = current.next

if __name__=="__main__":
    linked_list = DoublyLinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_ending(3)
    linked_list.print_ll()