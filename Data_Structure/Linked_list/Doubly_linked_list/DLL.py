class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList("deepak")
my_doubly_linked_list.append("rohan")
my_doubly_linked_list.append("sohan")
my_doubly_linked_list.append("ashok")
my_doubly_linked_list.append("ram")
my_doubly_linked_list.insert(0,"test")

# print('Get node from first half of DLL:')
# print(my_doubly_linked_list.get(1).value)

# print('\nGet node from second half of DLL:')
# print(my_doubly_linked_list.get(2).value)
# print(my_doubly_linked_list.set_value(1, 22))

# (2) Items - Returns 2 Node
# print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
# print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
# print(my_doubly_linked_list.pop_first())
# print('Before prepend():')
# print('----------------')
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length, '\n')
# print('Doubly Linked List:')
# my_doubly_linked_list.print_list()

# my_doubly_linked_list.prepend(1)


# print('\n\nAfter prepend():')
# print('---------------')
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length, '\n')
# print('Doubly Linked List:')
my_doubly_linked_list.print_list()

# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop())
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length)
