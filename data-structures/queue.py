"""
    A Queue is a linear data structure that operates according to the FIFO principle.
    This is an implementation of a Queue using a linked list. 
"""

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.rear = new_node
        self.length = 1

    def enqueue(self, value):
        temp = Node(value)
        if self.is_empty():
            self.front = temp
        else:
            self.rear.next = temp

        self.rear = temp
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.front.value

        if self.length == 1:    
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        self.length -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            return None

        return self.front.value

    def size(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0

    def print(self):
        temp = self.front
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None") 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print()
print("Peek: ", my_queue.peek())
print("Length: ", my_queue.size())
print("isEmpty ? : ", my_queue.is_empty(), "\n")

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()
print("Peek: ", my_queue.peek())
print("Length: ", my_queue.size())
print("isEmpty ? : ", my_queue.is_empty(), "\n")

my_queue.dequeue()
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print()
print("Peek: ", my_queue.peek())
print("Length: ", my_queue.size())
print("isEmpty ? : ", my_queue.is_empty(), "\n")

