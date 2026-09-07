# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduced Binary Search Trees (BSTs) and recursive tree operations.

# Learning Objectives

Built a BST

Inserted values recursively

Searched recursively

Performed in-order traversal

Demonstrated an understanding of BST organization

# Requirements Completed

Built a BST.

Inserted multiple values into both the left and right subtrees.

Demonstrated in-order traversal.

Tested searches for values that existed and values that did not exist.

Demonstrated edge cases using an empty tree and a duplicate value.

Used employee ID organization as a real-world BST example.

# Program Design

I created a Node class to store a value and references to left and right child nodes. I created a BST class with recursive insertion, recursive searching, and in-order traversal methods. Smaller values were inserted into the left subtree, while larger values were inserted into the right subtree. Duplicate values were ignored so that the existing tree structure remained unchanged.

The program inserted the values 50, 30, 70, 20, 40, 60, and 80. This insertion order created both left and right subtrees and produced a balanced example.

The in-order traversal produced:

[20, 30, 40, 50, 60, 70, 80]

Search tests were completed for existing values 40 and 70 and missing values 25 and 90.

# Real-World BST

A Binary Search Tree could be used to organize employee records by employee ID. IDs smaller than the current employee ID could be stored in the left subtree, while larger IDs could be stored in the right subtree. This organization could make searches more efficient when the tree remained reasonably balanced.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.