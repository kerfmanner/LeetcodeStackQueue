'''Frequency Stack
I've chosen defaultdict from collections to handle 
frequency counts, and heapq for the priority queue.
Defaultdict is just a fancy common dict and it's just used to count the frequency of elements.
On the other hand, heapq is the core of this implementation. It is used to create a priority queue,
using the frequency, that is stored in defaultdict, counter to remember which value was added later, 
and value in a tuple of three elements.
The first two elements are negative because heapq is a min-heap,
and we want to pop the maximum frequency first.
This makes time complexity O(log n) for push and pop operations, I believe.
'''
import heapq
import itertools
from collections import defaultdict


class FreqStack:
    '''A stack that supports push and pop operations with frequency tracking.'''
    def __init__(self):
        self.frequencies = defaultdict(int)
        self.items = []
        self.counter = itertools.count()

    def push(self, value):
        '''Push a value onto the stack, updating its frequency.'''
        freq = self.frequencies[value] + 1
        self.frequencies[value] = freq
        heapq.heappush(self.items, (-freq, -next(self.counter), value))

    def pop(self):
        '''Pop the most frequent value from the stack.'''
        if not self.items:
            raise IndexError
        _, _, value = heapq.heappop(self.items)
        self.frequencies[value] = max(0, self.frequencies[value] - 1)
        return value
