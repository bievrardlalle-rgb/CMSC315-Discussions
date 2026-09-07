"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Start at the root and use the recursive helper to find
        # the correct location for the new value.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If there is no node at this position, create one.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are not inserted. The existing node is kept.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST can reduce the search space at each comparison because
        # values smaller than a node are on the left and larger values
        # are on the right. This can be faster than checking every item.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: reaching an empty position means the value was not found.
        if node is None:
            return False

        # If the current node contains the target value, the search is complete.
        if value == node.value:
            return True

        # Search only the subtree where the target could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visit the left subtree first because it contains smaller values.
        self._inorder_recursive(node.left, values)

        # Visit the current node after all smaller values.
        values.append(node.value)

        # Visit the right subtree last because it contains larger values.
        self._inorder_recursive(node.right, values)

        # Visiting left, current, then right produces sorted output in a BST.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Create the BST and insert values in an order that creates
    # both left and right subtrees.
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for value in values_to_insert:
        tree.insert(value)

    print("Values inserted:", values_to_insert)

    # A BST reduces the search space because each comparison tells us
    # whether to continue left or right instead of checking every node.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    traversal = tree.inorder()
    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree, current node, and
    # right subtree. Because of BST ordering, the result is sorted.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # These values exist in the tree, so the results should be True.
    print("Search for 40:", tree.search(40))
    print("Search for 70:", tree.search(70))

    # These values were never inserted, so the results should be False.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Create an empty BST to show that traversal returns an empty list
    # and searching an empty tree safely returns False.
    empty_tree = BST()
    print("Empty tree traversal:", empty_tree.inorder())
    print("Search empty tree for 10:", empty_tree.search(10))

    # Insert a duplicate value. This implementation ignores duplicates,
    # so the tree structure and in-order output remain unchanged.
    tree.insert(50)
    print("After attempting to insert duplicate 50:", tree.inorder())


if __name__ == "__main__":
    main()
