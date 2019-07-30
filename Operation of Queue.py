# CLass Queue

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.capacity == self.size

    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue
    # It changes the rear and size
    def EnQueue(self,item):
        if self.isFull():
            print("It's full.")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print ("%s enqueued to queue" %str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("It's empty.")
            return
        print("%s dequeued from queue" % str(self.Q[self.fron]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Empty")
        print("Front item is", self.Q[self.front])
    def que_rear(self):
        if self.isEmpty():
            print("Empty")
        print("Rear item is", self.Q[self.rear])


if __name__ == '__main__':
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()