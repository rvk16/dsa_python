class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None

        current_node = self.head
        previous_node = self.head

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        self.tail = previous_node
        self.tail.next = None
        self.length -= 1

        if self.length == 0: #This is when we have one item in the list
            self.head = None
            self.tail = None
        return current_node


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None

        current_node = self.head
        self.head = self.head.next
        current_node.next = None
        self.length -= 1

        if self.length == 0:    #This is when we have one item in the list
            self.tail = None
        return current_node.value


    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node


    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        current_node.value = value



    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0 :
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        previous_node = self.get(index - 1)
        current_node = previous_node.next

        previous_node.next = current_node.next
        current_node.next = None
        self.length -= 1
        return current_node


    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.set_value(1, 5)
my_linked_list.print_list()