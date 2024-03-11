# In a normal queue, after a bit of insertion and deletion, there will be non-usable empty space.

# Circular Queue implementation in Python

class MyCircularQueue():

    def __init__(self, k):
        # Constructor method to initialize the circular queue
        self.k = k  # Maximum size of the circular queue
        self.queue = [None] * k  # Initializing an array to represent the circular queue
        self.head = self.tail = -1  # Initializing head and tail pointers to -1, indicating an empty queue

    # Insert an element into the circular queue
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            # Check if the next position after tail is equal to head, indicating the circular queue is full
            print("The circular queue is full\n")
        elif (self.head == -1):
            # If the queue is empty, set head and tail to 0 and insert the element
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            # Move the tail to the next position (circularly) and insert the element
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            # Check if the queue is empty
            print("The circular queue is empty\n")
        elif (self.head == self.tail):
            # If there is only one element in the queue, reset head and tail
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            # Remove the element at the head and move the head to the next position (circularly)
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            # Check if the queue is empty
            print("No element in the circular queue")
        elif (self.tail >= self.head):
            # If tail is ahead of head, print elements from head to tail
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            # If tail is behind head, print elements from head to the end and then from the beginning to tail
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()