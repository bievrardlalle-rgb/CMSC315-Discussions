"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each item from beginning to end.
    # In the worst case, every item must be checked.
    # Therefore, linear search has O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 when the target does not exist in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Set the beginning and ending indexes of the search area.
    low = 0
    high = len(lst) - 1

    while low <= high:

        # Find the middle index of the remaining search area.
        mid = (low + high) // 2

        # If the middle value matches the target, return its index.
        if lst[mid] == target:
            return mid

        # If the target is larger than the middle value,
        # eliminate the left half of the remaining list.
        elif lst[mid] < target:
            low = mid + 1

        # If the target is smaller than the middle value,
        # eliminate the right half of the remaining list.
        else:
            high = mid - 1

        # Each iteration removes approximately half of the
        # remaining search area, giving binary search O(log n)
        # time complexity.

    # Return -1 when the target does not exist in the list.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted dataset of student scores.
    small_scores = [55, 67, 72, 81, 90, 95]

    # Search for a score that exists.
    existing_score = 81

    linear_result = linear_search(small_scores, existing_score)
    binary_result = binary_search(small_scores, existing_score)

    print("Student scores:", small_scores)
    print("Searching for existing score:", existing_score)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both searches should return index 3 because 81 is
    # located at index 3 in the list.

    # Search for a score that does not exist.
    missing_score = 85

    linear_missing = linear_search(small_scores, missing_score)
    binary_missing = binary_search(small_scores, missing_score)

    print("\nSearching for missing score:", missing_score)
    print("Linear search result:", linear_missing)
    print("Binary search result:", binary_missing)
    print("-1 means the score was not found.")

    # Both searches return -1 because 85 is not in the list.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a large sorted dataset containing values 1 through 10,000.
    large_dataset = list(range(1, 10001))

    # Search for a value near the end of the dataset.
    large_target = 9999

    large_linear_result = linear_search(large_dataset, large_target)
    large_binary_result = binary_search(large_dataset, large_target)

    print("Dataset size:", len(large_dataset))
    print("Searching for:", large_target)
    print("Linear search index:", large_linear_result)
    print("Binary search index:", large_binary_result)

    # Linear search may have to examine almost every element to find
    # a value near the end of the list.
    #
    # Binary search repeatedly eliminates half of the remaining data,
    # making it much more efficient for large sorted datasets.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    # Neither search algorithm has any values to examine,
    # so both should safely return -1.
    empty_list = []

    print("Empty list - Linear search:",
          linear_search(empty_list, 81))
    print("Empty list - Binary search:",
          binary_search(empty_list, 81))

    # Edge Case 2: Single-element list
    # The only value should be found immediately at index 0.
    single_score = [81]

    print("\nSingle-element list - Linear search:",
          linear_search(single_score, 81))
    print("Single-element list - Binary search:",
          binary_search(single_score, 81))

    # Additional Edge Case: value at the first position.
    first_score = 55

    print("\nFirst-position score - Linear search:",
          linear_search(small_scores, first_score))
    print("First-position score - Binary search:",
          binary_search(small_scores, first_score))

    # Additional Edge Case: value at the last position.
    last_score = 95

    print("\nLast-position score - Linear search:",
          linear_search(small_scores, last_score))
    print("Last-position score - Binary search:",
          binary_search(small_scores, last_score))

    # ==================================
    # REAL-WORLD SEARCH SCENARIO
    # ==================================

    print("\n=== REAL-WORLD STUDENT SCORE LOOKUP ===")

    # A student information system could use a search algorithm
    # to locate a particular score in stored student score data.
    student_scores = [60, 68, 75, 81, 87, 92, 98]
    score_to_find = 87

    result = binary_search(student_scores, score_to_find)

    if result != -1:
        print("Score", score_to_find,
              "was found at index", result)
    else:
        print("Score", score_to_find, "was not found.")


if __name__ == "__main__":
    main()