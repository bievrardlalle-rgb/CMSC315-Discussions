"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Insert the value at the specified index.
    # Existing elements at and after this index shift one position to the right.
    # Inserting near the beginning can take more time because more elements
    # may need to shift than when inserting near the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Check that the index is within the valid range of the list.
    # Validating the index prevents an error when attempting to delete
    # an element that does not exist.
    if 0 <= index < len(lst):
        # pop() removes and returns the value at the specified index.
        return lst.pop(index)

    # Return None if the index is invalid.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each element is checked
    # sequentially from the beginning of the list.
    # If the value is near the end or missing, every element may be checked.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 if the value is not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # This list represents support ticket numbers in a help desk system.
    tickets = [101, 102, 103, 104]
    print("Original ticket list:", tickets)

    # Insert a priority ticket at the beginning.
    insert_at(tickets, 0, 100)
    print("After insertion at beginning:", tickets)

    # Insert a ticket near the middle of the list.
    insert_at(tickets, 2, 105)
    print("After insertion in middle:", tickets)

    # Insert a ticket at the end of the list.
    insert_at(tickets, len(tickets), 106)
    print("After insertion at end:", tickets)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete the first ticket in the list.
    removed = delete_at(tickets, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", tickets)

    # Delete a ticket from the middle of the list.
    middle_index = len(tickets) // 2
    removed = delete_at(tickets, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", tickets)

    # Delete the final ticket in the list.
    removed = delete_at(tickets, len(tickets) - 1)
    print("Removed from end:", removed)
    print("Updated list:", tickets)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a ticket number that exists in the list.
    existing_ticket = 102
    result = search_value(tickets, existing_ticket)

    if result != -1:
        print(f"Ticket {existing_ticket} was found at index {result}.")
    else:
        print(f"Ticket {existing_ticket} was not found.")

    # Search for a ticket number that does not exist.
    missing_ticket = 999
    result = search_value(tickets, missing_ticket)

    if result != -1:
        print(f"Ticket {missing_ticket} was found at index {result}.")
    else:
        print(f"Ticket {missing_ticket} was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1:
    # Attempt to delete an item using an invalid index.
    # The function safely returns None rather than causing an error.
    invalid_delete = delete_at(tickets, 100)
    print("Delete using invalid index:", invalid_delete)

    # Edge Case 2:
    # Insert a value into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 200)
    print("Insert into empty list:", empty_list)

    # Edge Case 3:
    # Attempt to delete from an empty list.
    empty_delete = delete_at([], 0)
    print("Delete from empty list:", empty_delete)

    # Edge Case 4:
    # Search for a value in an empty list.
    empty_search = search_value([], 500)
    print("Search in empty list:", empty_search)


if __name__ == "__main__":
    main()