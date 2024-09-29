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
            return None
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


def find_kth_from_end(my_linked_list, k):
    slow_pointer = my_linked_list.head
    fast_pointer = my_linked_list.head

    for _ in range(k):
        if fast_pointer is None:
            return None
        fast_pointer = fast_pointer.next

    while fast_pointer is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2

print(find_kth_from_end(my_linked_list,k))