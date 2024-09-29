# Reversing the linked list

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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def reverse_linked_list(self):
        current_node = self.head
        self.head = self.tail
        self.tail = current_node

        before_node = None

        for _ in range(self.length):
            after_node = current_node.next
            current_node.next = before_node
            before_node = current_node
            current_node = after_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


my_linked_list = LinkedList(5)
my_linked_list.append(6)
my_linked_list.append(8)

my_linked_list.reverse_linked_list()
my_linked_list.print_list()
