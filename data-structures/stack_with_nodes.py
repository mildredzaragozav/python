"""
    A stack is a data structure where elements are inserted and removed according to the LIFO principle.
    This is an implementation of a stack using a nodes. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        temp = Node(value)
        temp.next = self.top
        self.top = temp
        self.height += 1

    def pop(self):
        if self.is_empty(): return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value

    def peek(self):
        if self.is_empty(): return None
        
        return self.top.value

    def size(self):
        return self.height

    def is_empty(self):
        return self.height == 0

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None") 


my_stack = Stack(10)
my_stack.push(20)
my_stack.push(30)
my_stack.print()
print("Peek: ", my_stack.peek())
print("Size: ", my_stack.size())
print("isEmpty ? : ", my_stack.is_empty(), "\n")

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print()
print("Peek: ", my_stack.peek())
print("Size: ", my_stack.size())
print("isEmpty ? : ", my_stack.is_empty(), "\n")

my_stack.pop()
my_stack.push(50)
my_stack.print()
print("Peek: ", my_stack.peek())
print("Size: ", my_stack.size())
print("isEmpty ? : ", my_stack.is_empty(), "\n")