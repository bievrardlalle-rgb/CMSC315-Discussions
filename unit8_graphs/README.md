# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explored graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represented graphs using adjacency lists
- Implemented BFS
- Used queues in graph traversal
- Analyzed graph traversal behavior

## Requirements Completed

1. Created a graph using an adjacency list.
2. Performed BFS traversal starting from Movie A.
3. Added Movie G and connected it to Movie D.
4. Demonstrated edge cases involving a missing node, a single-node graph,
   and an empty graph.
5. Analyzed how BFS visited nodes level by level.
6. Created a real-world streaming recommendation graph.

## Program Description

I created a graph that represented relationships between movies in a
streaming recommendation system. Each movie represented a vertex, while
connections between movies represented edges based on similar genres,
actors, ratings, or viewer preferences.

I implemented Breadth-First Search using a deque as a queue and a set to
track visited nodes. The queue allowed the program to process nodes in
first-in, first-out order. This caused BFS to explore nearby connections
before moving to nodes farther away.

I also added another movie to the graph and ran BFS again to demonstrate
how a new vertex and edge affected the traversal. Finally, I tested
multiple edge cases to ensure the program handled unusual inputs safely.

## Discussion Board Reflection

While completing this assignment, I learned how graphs can represent relationships between connected data and how Breadth-First Search can be used to traverse those relationships. I created an adjacency list using a Python dictionary where each movie represented a node and its related movies represented neighboring nodes. I also learned how a queue and visited set work together during BFS. The queue maintains the order in which nodes are explored, while the visited set prevents the program from repeatedly processing the same node.

One challenge I encountered was understanding when a node should be marked as visited. I learned that marking it as visited when it is added to the queue prevents duplicate entries and makes the traversal more efficient. Testing missing nodes, an empty graph, and a single-node graph also helped me understand important edge cases.

BFS and DFS both traverse graphs, but they use different strategies. BFS explores nearby nodes level by level, making it useful for shortest-path and recommendation problems involving close connections. DFS explores one path deeply before backtracking, making it useful for maze solving, dependency analysis, and exploring deeper relationships.