# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

I implemented both linear search and binary search in Python. The linear
search algorithm examined each value in the list from beginning to end
until the target value was found. If the target was not found, the
algorithm returned -1.

I implemented binary search using low, high, and middle indexes. Because
the datasets used with binary search were sorted, the algorithm compared
the target with the middle value and eliminated approximately half of the
remaining search area after each comparison.

## Small Dataset Testing

I created a small sorted dataset containing student scores:

55, 67, 72, 81, 90, 95

I tested both linear search and binary search using a score that existed
in the dataset and a score that did not exist. Both algorithms correctly
returned the index of the existing score and returned -1 when the missing
score was searched for.

## Large Dataset Testing

I created a larger sorted dataset containing values from 1 through
10,000. I searched for a value near the end of the dataset using both
algorithms.

The test demonstrated that linear search could require checking many
values before finding a target near the end of a large list. Binary
search reduced the remaining search area by approximately half after
each comparison, making it more efficient for large sorted datasets.

## Edge Cases

I tested several edge cases to verify that the algorithms handled
different situations correctly.

- I tested an empty list, and both algorithms returned -1.
- I tested a single-element list, and both algorithms returned index 0
  when the target was present.
- I searched for a value in the first position of the dataset, and both
  algorithms returned index 0.
- I searched for a value in the last position of the dataset, and both
  algorithms returned index 5.

These tests demonstrated that both search methods handled boundary
conditions and empty datasets correctly.

## Real-World Application

I created a student score lookup scenario to demonstrate a real-world
application of searching algorithms. I used binary search to locate a
specific score in a sorted collection of student scores. The program
successfully located score 87 at index 4.

A similar approach could be used in student information systems to
retrieve information efficiently from organized datasets.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.