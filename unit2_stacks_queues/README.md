# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Summary

I implemented the Stack class using a Python list to store values. I completed the push, pop, peek, and is_empty operations and demonstrated LIFO behavior by showing that the most recently added item was removed first.

I implemented the Queue class using collections.deque. I completed the enqueue, dequeue, front, and is_empty operations and demonstrated FIFO behavior by showing that the first item added to the queue was removed first.

I also tested several edge cases, including popping and peeking from an empty stack, dequeuing and viewing the front of an empty queue, and verifying that single-item stacks and queues became empty after their items were removed.

For the real-world scenario, I created an IT help-desk ticket queue. Support tickets were added to the queue and processed in the order they were received, demonstrating how FIFO behavior can be applied to a real-world IT support environment.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
