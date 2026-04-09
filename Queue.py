from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue operation (add element to rear)
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Safe dequeue operation (remove element from front)
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            removed_item = self.queue.popleft()
            print(f"Dequeued: {removed_item}")
            return removed_item

    # Display queue elements
    def display(self):
        print("Queue:", list(self.queue))

# Example usage
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.safe_dequeue()
q.safe_dequeue()

# Display remaining
q.display()