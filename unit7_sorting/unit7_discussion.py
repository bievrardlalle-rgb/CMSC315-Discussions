"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Create a copy of the original list so it is not modified.
    sorted_list = lst.copy()

    # Loop through the list multiple times.
    for i in range(len(sorted_list) - 1):

        # Track whether any values were swapped during this pass.
        swapped = False

        # Compare adjacent values in the list.
        for j in range(len(sorted_list) - 1 - i):

            # If the current value is greater than the next value,
            # swap them so the smaller value moves toward the front.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    # Return the sorted copy of the list.
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Base case:
    # A list containing zero or one item is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle position of the list.
    middle = len(lst) // 2

    # Divide the list into a left half and a right half.
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge both sorted halves and return the result.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    # Create a list that will store the merged values.
    result = []

    # Create indexes for tracking positions in both lists.
    left_index = 0
    right_index = 0

    # Compare values while both lists still contain items.
    while left_index < len(left) and right_index < len(right):

        # Add the smaller value to the result list.
        # Using <= also helps maintain stability when values are equal.
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    result.extend(left[left_index:])

    # Add any remaining values from the right list.
    result.extend(right[right_index:])

    # Return the completed sorted list.
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # Dataset #1 contains eight unsorted values.
    dataset1 = [45, 12, 78, 34, 23, 89, 5, 67]

    # Display the original unsorted dataset.
    print("Original List:", dataset1)

    # Sort Dataset #1 using Bubble Sort.
    bubble_result1 = bubble_sort(dataset1)

    # Sort Dataset #1 using Merge Sort.
    merge_result1 = merge_sort(dataset1)

    # Display the results.
    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # Compare the results from both algorithms.
    print(
        "Both algorithms produced the same result:",
        bubble_result1 == merge_result1
    )

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    # Dataset #2 contains different unsorted values.
    dataset2 = [91, 56, 14, 72, 38, 6, 50, 27]

    # Display the original dataset.
    print("Original List:", dataset2)

    # Sort Dataset #2 using Bubble Sort.
    bubble_result2 = bubble_sort(dataset2)

    # Sort Dataset #2 using Merge Sort.
    merge_result2 = merge_sort(dataset2)

    # Display the results.
    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    # Compare the results from both sorting algorithms.
    print(
        "Both algorithms produced the same result:",
        bubble_result2 == merge_result2
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # -------------------------------------------------------
    # Edge Case #1: Empty List
    # -------------------------------------------------------

    empty_list = []

    print("\nEdge Case #1 - Empty List")
    print("Original List:", empty_list)

    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))

    print(
        "Explanation: The empty list remains empty because "
        "there are no values that need to be sorted."
    )

    # -------------------------------------------------------
    # Edge Case #2: Already Sorted List
    # -------------------------------------------------------

    already_sorted = [10, 20, 30, 40, 50]

    print("\nEdge Case #2 - Already Sorted List")
    print("Original List:", already_sorted)

    print("Bubble Sort:", bubble_sort(already_sorted))
    print("Merge Sort:", merge_sort(already_sorted))

    print(
        "Explanation: Both algorithms return the same order "
        "because the values were already sorted."
    )

    # -------------------------------------------------------
    # Edge Case #3: Duplicate Values
    # -------------------------------------------------------

    duplicate_values = [8, 3, 8, 2, 3, 1]

    print("\nEdge Case #3 - Duplicate Values")
    print("Original List:", duplicate_values)

    print("Bubble Sort:", bubble_sort(duplicate_values))
    print("Merge Sort:", merge_sort(duplicate_values))

    print(
        "Explanation: Both algorithms correctly sort the list "
        "while keeping all duplicate values."
    )

    # -------------------------------------------------------
    # Real-World Sorting Example
    # -------------------------------------------------------

    print("\n=== REAL-WORLD SORTING EXAMPLE ===")

    # This example represents ratings for content on a
    # streaming platform that need to be displayed in order.
    content_ratings = [4.7, 3.9, 4.9, 4.2, 3.8, 4.5, 4.1]

    print("Original Content Ratings:", content_ratings)

    bubble_ratings = bubble_sort(content_ratings)
    merge_ratings = merge_sort(content_ratings)

    print("Bubble Sort Ratings:", bubble_ratings)
    print("Merge Sort Ratings:", merge_ratings)

    print(
        "Explanation: A streaming platform could sort content "
        "ratings before displaying movies or shows to users."
    )


if __name__ == "__main__":
    main()