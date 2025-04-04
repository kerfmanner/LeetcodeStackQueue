'''Implement Queue using Stacks'''        
class Node:
    '''A node class for linked list implementation.'''
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    '''A simple stack implementation using a linked list.'''
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        '''Check if the stack is empty.'''
        return self.size == 0

    def push(self, item):
        '''Push an item onto the stack.'''
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        '''Return the top item of the stack and remove it."""'''
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        '''Return the top item of the stack without removing it."""'''
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

class MyQueue:
    '''Implementation of a queue using stacks.'''
    def __init__(self):
        self.mainstack = StackLinkedList()
        self.storestack = StackLinkedList()

    def push(self, x: int) -> None:
        '''Push an item onto the queue.'''
        self.mainstack.push(x)

    def pop(self) -> int:
        '''Return the front element of the queue and remove it.'''
        if self.empty():
            return None

        while not self.empty():
            element = self.mainstack.pop()
            self.storestack.push(element)
        first = self.storestack.pop()

        while not self.storestack.is_empty():
            element = self.storestack.pop()
            self.mainstack.push(element)
        return first

    def peek(self) -> int:
        '''Return the front item of the queue without removing it.'''
        if self.empty():
            return None

        while not self.empty():
            element = self.mainstack.pop()
            self.storestack.push(element)
        first = self.storestack.peek()

        while not self.storestack.is_empty():
            element = self.storestack.pop()
            self.mainstack.push(element)
        return first


    def empty(self) -> bool:
        '''Check if the queue is empty.'''
        return self.mainstack.is_empty()

