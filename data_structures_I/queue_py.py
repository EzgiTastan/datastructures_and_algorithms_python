# A queue is an object (an abstract data structure - ADT) that allows the following operations:
# Enqueue: Add an element to the end of the queue
# Dequeue: Remove an element from the front of the queue
# IsEmpty: Check if the queue is empty
# IsFull: Check if the queue is full
# Peek: Get the value of the front of the queue without removing it

# Queue implementation in Python

class Queue:

# the __init__method creates an empty list at first.
    def __init__(self):
        self.queue = []

#the enqueue method adds an item to the queue.    self.queue.append(item)
    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Define another function called dequeue. If there is not any elements (if len(self.queue) < 1), return None!
    #else, keep popping. The element in the first index will be removed.
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
