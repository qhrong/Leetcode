# Using Array to Implement
# import maxsize from sys module
from sys import maxsize

# Funtion to create a stack
def createStack():
    stack = []
    return stack

# Function to detect if stack is empty
def isEmpty(stack):
    return len(stack)==0

# Function to add an item
def push(stack, item):
    stack.append(item)
    print(item + " is pushed to the stack.")

# Function to remove an item, decreasing the size by 1
def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize - 1) # minus infinite

    return stack.pop()

# Function to return the top from stack, without changing the size
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)

    return stack[len(stack) - 1]

# Test
stack = createStack()
push(stack, str(10))
push(stack, str(20))
print(pop(stack) + " popped from stack")

# ----------------------------------------------------------------------------

# Using Linked List to Implement

# Class to represent a new node
class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

# Class to operate the stack
class Stack:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print("% is pushed to stack" % data )

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next # delete popped item from stack
        return temp.data

    def peek(self):
        if (self.isEmpty()):
            return float("-inf")
        return self.root.data # doesn't need to delete the popped item

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()