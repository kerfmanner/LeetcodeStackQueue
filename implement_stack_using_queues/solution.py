'''Leetcode 225. Implement Stack using Queues'''
class Node:
    '''A node class for linked list implementation.'''
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    ''''Queue implementation using linked list'''
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        '''Check if the queue is empty.'''
        return self.size == 0

    def push(self, item):
        '''Push an item onto the queue.'''
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        '''Return the front item of the queue and remove it.'''
        if self.is_empty():
            raise IndexError("pop from empty queue")
        popped_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return popped_node.data

    def peek(self):
        '''Return the front item of the queue without removing it.'''

        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self.front.data


class MyStack:
    '''''Implementation of a stack using a queue.'''

    def __init__(self):
        self.items = QueueLinkedList()

    def push(self, x: int) -> None:
        '''Push an item onto the stack.'''
        self.items.push(x)

    def pop(self) -> int:
        '''Return the top element of the stack and remove it.'''

        if self.empty():
            return None

        count = 0

        while count < self.items.size:

            count += 1

            if count == self.items.size:
                return self.items.pop()

            element = self.items.pop()
            self.items.push(element)

    def top(self) -> int:
        '''Return the top element of the stack without removing it.'''

        if self.empty():
            return None

        count = 0

        while count < self.items.size:
            element = self.items.pop()
            self.items.push(element)
            count += 1

        return element

    def empty(self) -> bool:
        '''Check if the stack is empty.'''
        return self.items.is_empty()
