"""
    A stack is a data structure where elements are inserted and removed according to the LIFO principle.
    This is an implementation of a stack using a list. 
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0 

    def print(self):
        print(self.stack[::-1])

        
my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print()

print("pop: ", my_stack.pop())
print("Current peek: ", my_stack.peek()) 

print("pop: ", my_stack.pop())
my_stack.push(4)
my_stack.print()

print("pop: ", my_stack.pop())
print("pop: ", my_stack.pop())

print("Size: ", my_stack.size()) #Expected: 'Size: 0'
print("isEmpty ? ", my_stack.is_empty()) #Expected: isEmpty ? True
