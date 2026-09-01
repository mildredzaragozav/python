'''
    A deque is a linear data structure that allows us to insert and remove elements from both ends of it.
    This is an implementation of deque using a doubly linked list.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.back = new_node
        self.length = 1

    '''Insert operations'''

    def add_front(self, value):
        temp = Node(value)

        if self.length == 0:
            self.back = temp
        else:
            self.front.prev = temp    
            temp.next = self.front

        self.front = temp
        self.length += 1

    def add_back(self, value):
        temp = Node(value)
        if self.length == 0:
            self.front = temp
        else:
            temp.prev = self.back
            self.back.next = temp 

        self.back = temp
        self.length += 1

    '''Remove operations'''

    def remove_front(self):
        if self.length == 0:
            return None

        temp = self.front
        if self.length == 1:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
            temp.next = None

        self.length -= 1
        return temp.value

    def remove_back(self):
        if self.length == 0:
            return None

        temp = self.back
        if self.length == 1:
            self.front = None
            self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
            temp.prev = None

        self.length -= 1
        return temp.value

    '''Examine operations'''

    def get_front(self):
        if self.length == 0:
            return None

        return self.front.value

    def get_back(self):
            if self.length == 0:
                return None
    
            return self.back.value

    '''Util operations'''

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def print(self):
        current = self.front
        output = []
        while current is not None:
            output.append(str(current.value))
            current = current.next
        print(" <-> ".join(output))

    def print_reverse(self):
        current = self.back
        output = []
        while current is not None:
            output.append(str(current.value))
            current = current.prev
        print(" <-> ".join(output))


my_deque = Deque(10)
my_deque.add_front(9)
my_deque.print() # 9 - 10
my_deque.print_reverse()
print("Front: ", my_deque.get_front())
print("Back: ", my_deque.get_back())
print("Size: ", my_deque.size())
print("isEmpty ? : ", my_deque.is_empty(), "\n")

my_deque.remove_front()
my_deque.remove_back()
my_deque.print() # None
my_deque.print_reverse()
print("Front: ", my_deque.get_front())
print("Back: ", my_deque.get_back())
print("Size: ", my_deque.size())
print("isEmpty ? : ", my_deque.is_empty(), "\n")

my_deque.add_back(11)
my_deque.add_front(10)
my_deque.add_back(12)
my_deque.print() # 10 - 11 - 12
my_deque.print_reverse()
print("Front: ", my_deque.get_front())
print("Back: ", my_deque.get_back())
print("Size: ", my_deque.size())
print("isEmpty ? : ", my_deque.is_empty(), "\n")

my_deque.remove_back()
my_deque.remove_back()
my_deque.remove_back()
my_deque.remove_front()
my_deque.print() # None
my_deque.print_reverse()
print("Front: ", my_deque.get_front())
print("Back: ", my_deque.get_back())
print("Size: ", my_deque.size())
print("isEmpty ? : ", my_deque.is_empty(), "\n")



