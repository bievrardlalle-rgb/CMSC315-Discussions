"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node does not exist, return an empty list.
    if start not in graph:
        return []

    # The queue stores nodes that still need to be explored.
    # A queue uses FIFO order, allowing BFS to visit nodes
    # level by level.
    queue = deque([start])

    # The visited set prevents the same node from being
    # processed multiple times.
    visited = {start}

    # This list stores the final BFS traversal order.
    traversal_order = []

    # Continue searching while there are nodes in the queue.
    while queue:
        # Remove the node at the front of the queue.
        current = queue.popleft()
        traversal_order.append(current)

        # Check each neighbor connected to the current node.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                # Mark the neighbor as visited before adding it
                # to the queue so it is not added multiple times.
                visited.add(neighbor)

                # Neighbors are added to the queue so BFS can
                # explore them in FIFO, level-by-level order.
                queue.append(neighbor)

    # BFS explores nearby nodes before moving farther away.
    # DFS differs because it follows one path as deeply as
    # possible before backtracking.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents a streaming recommendation network.
    # Each node represents a movie or TV show.
    # Each edge represents a relationship based on similar genres,
    # actors, ratings, or viewer preferences.
    graph = {
        "Movie A": ["Movie B", "Movie C"],
        "Movie B": ["Movie A", "Movie D", "Movie E"],
        "Movie C": ["Movie A", "Movie F"],
        "Movie D": ["Movie B"],
        "Movie E": ["Movie B", "Movie F"],
        "Movie F": ["Movie C", "Movie E"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    # print("TODO: Create and display a graph.")

    # Display every node and its neighboring nodes.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    # print("TODO: Perform and explain BFS traversal.")

    # Start BFS at Movie A.
    # BFS first visits Movie A, followed by its immediate
    # neighbors, and then moves to nodes farther away.
    start_node = "Movie A"
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("Original BFS traversal:", traversal)

    # Add a new movie to demonstrate how changing the graph
    # affects the BFS traversal.
    graph["Movie G"] = ["Movie D"]
    graph["Movie D"].append("Movie G")

    print("\nAdded Movie G with a connection to Movie D.")

    # Run BFS again after modifying the graph.
    updated_traversal = bfs(graph, start_node)
    print("Updated BFS traversal:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1:
    # Attempt to start BFS from a node that does not exist.
    # The bfs() function safely returns an empty list.
    print("\nEdge Case 1: Missing starting node")
    missing_result = bfs(graph, "Movie Z")
    print("Traversal from Movie Z:", missing_result)

    # Edge Case 2:
    # A graph containing only one node has no neighbors.
    # BFS should simply visit that one node.
    print("\nEdge Case 2: Single-node graph")
    single_node_graph = {
        "Movie X": []
    }

    single_result = bfs(single_node_graph, "Movie X")
    print("Single-node traversal:", single_result)

    # Edge Case 3:
    # An empty graph contains no valid starting nodes.
    # BFS safely returns an empty traversal.
    print("\nEdge Case 3: Empty graph")
    empty_graph = {}
    empty_result = bfs(empty_graph, "Movie A")
    print("Empty graph traversal:", empty_result)


if __name__ == "__main__":
    main()