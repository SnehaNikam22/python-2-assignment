class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        # Add an element to the top of the stack
        self.stack.append(item)

    # Safe pop method
    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            item = self.stack.pop()
            print(f"Item {item} popped from stack")
            return item

    # Display stack
    def display(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

# Driver code
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(50)
s.display()

s.safe_pop()
s.safe_pop()
s.safe_pop()

# Trying to pop from empty stack
s.safe_pop()
s.safe_pop()
