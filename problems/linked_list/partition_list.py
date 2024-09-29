# input : 3 8 5 10 2 1 and x = 5
# output : 3 2 1 8 5 10

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end= ' ')
            current_node = current_node.next
        print()

    def partition_list(self, x):
        less_head = Node(0)
        greater_head = Node(0)

        less = less_head
        greater = greater_head
        current_node = self.head

        while current_node is not None:
            if current_node.value < x:
                less.next = current_node
                less = less.next
            else:
                greater.next = current_node
                greater = greater.next
            current_node = current_node.next

        greater.next = None
        less.next = greater_head.next
        self.head = less_head.next


my_linked_list = LinkedList(3)
my_linked_list.append(8)
my_linked_list.append(5)
my_linked_list.append(10)
my_linked_list.append(2)
my_linked_list.append(1)

my_linked_list.print_list()

my_linked_list.partition_list(5)
my_linked_list.print_list()


