# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior. I created an inventory system that stored product SKUs and quantities as key-value pairs.

## Learning Objectives

During this assignment, I:

* Inserted key-value pairs into a Python dictionary.
* Retrieved inventory quantities using SKU keys.
* Updated values associated with existing keys.
* Removed key-value pairs from the dictionary.
* Tested edge cases involving missing keys.
* Learned how Python dictionaries behave like hash tables.

## Implementation

I created an empty dictionary named `inventory` and added five inventory items. Each SKU was used as a key, while the quantity of the product was stored as its associated value.

I demonstrated lookup operations by retrieving the quantities associated with existing SKUs. I then updated the quantity of an existing SKU and displayed the dictionary before and after the change.

For the delete operation, I removed an existing SKU from the dictionary and displayed the inventory before and after the deletion.

I also tested edge cases. I attempted to look up a SKU that did not exist by using the `get()` method, which safely returned `None`. I also attempted to remove a missing SKU by first checking whether the key existed. This prevented the program from generating a `KeyError`.

## Real-World Scenario

The program represented a basic inventory management system. Product SKUs such as `P100`, `P200`, and `P300` were used as dictionary keys, while inventory quantities were stored as values.

Using a dictionary made it possible to quickly locate a product's quantity without searching through every inventory record individually. This demonstrated how hash tables can be useful in real-world inventory and warehouse management systems.

## Conclusion

This assignment helped me understand how dictionaries use key-value pairs to organize information efficiently. I practiced inserting, retrieving, updating, and deleting data while also learning how to safely handle missing keys. The inventory example demonstrated how hash tables can provide fast access to information in real-world software applications.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.