class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, element):
        if self.size == 0:
            self.head = self.tail = Node(element)
        else:
            self.tail.next = Node(element)
            self.tail = self.tail.next
        self.size += 1

    def first_out(self):
        if self.size == 0:
            return None
        else:
            temp_node = self.head
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp_node.value

    def first_show(self):
        if self.size == 0:
            return None
        else:
            return self.head.value

    def size_show(self):
        return self.size
