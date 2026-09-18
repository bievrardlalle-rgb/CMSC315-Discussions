
"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Create an empty dictionary.
    # A Python dictionary behaves like a hash table because it stores
    # information as key-value pairs and uses keys for fast access.
    inventory = {}

    # Add five SKU and quantity key-value pairs.
    # The SKU is the key, and the inventory quantity is the value.
    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 25
    inventory["P400"] = 12
    inventory["P500"] = 30

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Display the contents of the dictionary.
    print("Inventory after inserting items:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Dictionary values can be retrieved directly by using their keys.
    # Python uses the key to locate the associated value efficiently.
    p100_quantity = inventory["P100"]
    p300_quantity = inventory["P300"]

    # Display the results of the two successful lookups.
    print("P100 quantity:", p100_quantity)
    print("P300 quantity:", p300_quantity)

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Display the dictionary before updating P100.
    print("Before update:")
    print(inventory)

    # Assigning a new value to an existing key replaces the old value.
    # P100 already exists, so its quantity changes from 15 to 20.
    inventory["P100"] = 20

    # Display the dictionary after the update.
    print("After updating P100 quantity to 20:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Display the dictionary before deleting an item.
    print("Before deletion:")
    print(inventory)

    # The del statement removes both the key and its associated value.
    # P200 and its quantity will no longer exist in the dictionary.
    del inventory["P200"]

    # Display the dictionary after the deletion.
    print("After deleting P200:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Lookup a missing key.
    # The get() method safely searches for a key.
    # If P999 does not exist, it returns None instead of causing an error.
    missing_item = inventory.get("P999")

    print("Looking up missing SKU P999:")
    print("Result:", missing_item)

    # Edge Case 2: Safely delete a missing key.
    # First, check whether the key exists before attempting to delete it.
    # This prevents a KeyError from occurring.
    if "P999" in inventory:
        del inventory["P999"]
        print("P999 was removed.")
    else:
        print("P999 was not found, so nothing was removed.")

    # Display the final dictionary.
    print("\nFinal inventory:")
    print(inventory)


if __name__ == "__main__":
    main()



