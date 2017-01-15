
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data

    def set_next(self,node):
        self.next = node
    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.length=0 # Storing this to return length in O(1) time

    def get_length(self):
        if not self.head:
            return 0
        else:
            current = self.head
            count =0
            while current.next:
                count+=1
                current = current.next
        return count

    def sorted_insert(self,data):
        """
        sorted insert function
        :param data:
        :return:
        """
        if not self.head :
            self.head = Node(data)
            self.length += 1

        else :
            new_node = Node(data)
            if data < self.head.data :
                new_node.next = self.head
                self.head = new_node
            else :
                current = self.head
                while current.next and current.next.data < new_node.data :
                    current = current.next
                new_node.next = current.next
                current.next = new_node



    def insert_at_begining(self,data=None):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert_at_ending(self,data=None):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else :
            current = self.head
            while current.next:
                current = current.get_next()
            current.next = new_node
        self.length +=1

    def insert_at_position(self,data=None,position=0):
        new_node = Node(data)
        if not self.head and position >0 :
            return 'enter valid position'
        if position > self.length and position<0:
            return 'enter valid position'
        else:
            if position == 0:
                self.head = new_node
            else:
                current = self.head
                count = 0
                while count<position and not current:
                    current += current.get_next()
                    count +=1
                temp = current.get_next()
                current.next = new_node
                new_node.next = temp
                self.length +=1

    def delete_first_node(self):

        if not self.head :
            return 'list is empty'
        else :
            if self.length ==1:
                self.head = None
            else :
                self.head = self.head.get_next()
            self.length-=1

    def delete_last_node(self):

        if not self.head:
            return 'list is empty'
        else :
            if self.length == 1:
                self.head = None
            else :
                current = self.head
                prev = self.head
                while current.get_next() != Node:
                    prev = current
                    current = current.get_next()
                prev.next=None
                self.length -=1

    def delete_linkedlist(self):
        self.head = None

    def print_list(self):
        if not self.head :
            return
        else :
            if self.length == 1:
                print(self.head.data)
            else :
                current = self.head
                while current:
                    print(current.get_data())
                    current=current.get_next()

    def find_length(self):
        if not self.head :
            return 0
        else  :
            current = self.head
            length = 0
            while current :
                current = current.next
                length +=1
            return length


if __name__=="__main__":

    linked_list = LinkedList()

    for i in range(1,5):
        linked_list.insert_at_ending(i)
    #linked_list.print_list()

    print(linked_list.find_length())
    print(linked_list.length)

    l = LinkedList()

    for i in range(10,0,-1):
        l.sorted_insert(i)
    for i in range(15,20):
        l.sorted_insert(i)
    #l.print_list()

















