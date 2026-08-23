"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are added to the end, so the most recent value is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the newest value without changing the stack.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so older values remain at the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the oldest value without changing the queue.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    stack.push("Document 1")
    stack.push("Document 2")
    stack.push("Document 3")
    stack.push("Document 4")

    print("Added Document 1, Document 2, Document 3, and Document 4.")
    print("Current top value:", stack.peek())

    print("\nRemoving values demonstrates LIFO behavior:")
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())

    print("\nTesting an empty stack:")
    print("Pop from empty stack:", stack.pop())
    print("Peek at empty stack:", stack.peek())

    single_stack = Stack()
    single_stack.push("Only Item")

    print("\nTesting a single-item stack:")
    print("Removed:", single_stack.pop())
    print("Is the stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    queue.enqueue("Ticket 101")
    queue.enqueue("Ticket 102")
    queue.enqueue("Ticket 103")
    queue.enqueue("Ticket 104")

    print("Added Ticket 101, Ticket 102, Ticket 103, and Ticket 104.")
    print("Ticket at the front:", queue.front())

    print("\nProcessing tickets demonstrates FIFO behavior:")
    print("Processed:", queue.dequeue())
    print("Processed:", queue.dequeue())
    print("Processed:", queue.dequeue())
    print("Processed:", queue.dequeue())

    print("\nTesting an empty queue:")
    print("Dequeue from empty queue:", queue.dequeue())
    print("Front of empty queue:", queue.front())

    single_queue = Queue()
    single_queue.enqueue("Ticket 105")

    print("\nTesting a single-item queue:")
    print("Processed:", single_queue.dequeue())
    print("Is the queue empty?", single_queue.is_empty())

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== IT HELP-DESK SCENARIO ===")

    help_desk = Queue()

    help_desk.enqueue("Password Reset")
    help_desk.enqueue("Laptop Issue")
    help_desk.enqueue("Network Connection Issue")
    help_desk.enqueue("Software Installation")

    print("Four IT support tickets were added to the help-desk queue.")
    print("First ticket waiting:", help_desk.front())

    print("Technician processed:", help_desk.dequeue())
    print("Next ticket waiting:", help_desk.front())

    print("This demonstrates FIFO because the first ticket received")
    print("is the first ticket processed.")


if __name__ == "__main__":
    main()
