# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort. I implemented both sorting algorithms in Python and tested them using multiple datasets. I also tested edge cases and created a real-world sorting example to demonstrate how sorting algorithms could be used in a software application.

## Learning Objectives

- Implemented Bubble Sort
- Implemented Merge Sort
- Practiced using recursion and divide-and-conquer
- Compared algorithm efficiency
- Tested sorting algorithms with different datasets
- Demonstrated edge cases
- Applied sorting algorithms to a real-world example

## Bubble Sort

I implemented Bubble Sort by creating a copy of the original list and comparing adjacent values. When two values were out of order, I swapped their positions. I continued this process until the list was sorted.

I also used a `swapped` variable to determine whether any swaps occurred during a pass. If no swaps occurred, the algorithm stopped early because the list was already sorted.

Bubble Sort has an average and worst-case time complexity of O(n²). Because of this, it is generally more appropriate for smaller datasets.

## Merge Sort

I implemented Merge Sort using recursion and the divide-and-conquer approach. The algorithm divided the original list into smaller left and right halves. Each half was recursively sorted until the lists contained zero or one element.

I then used a separate `merge()` function to compare values from the two sorted halves and combine them into one sorted list.

Merge Sort has a time complexity of O(n log n), making it more efficient than Bubble Sort for larger datasets. However, Merge Sort requires additional memory when creating and merging the smaller lists.

## Dataset Testing

I tested both sorting algorithms using two different unsorted datasets.

### Dataset #1

Original:

[45, 12, 78, 34, 23, 89, 5, 67]

Sorted:

[5, 12, 23, 34, 45, 67, 78, 89]

Both Bubble Sort and Merge Sort produced the same sorted result.

### Dataset #2

Original:

[91, 56, 14, 72, 38, 6, 50, 27]

Sorted:

[6, 14, 27, 38, 50, 56, 72, 91]

Both algorithms again produced the same sorted result.

## Edge Cases

I tested multiple edge cases to make sure both algorithms worked correctly.

### Empty List

I tested an empty list. Both Bubble Sort and Merge Sort returned an empty list without producing an error.

### Already Sorted List

I tested an already sorted list:

[10, 20, 30, 40, 50]

Both algorithms returned the values in the same order. Bubble Sort was able to stop early because no swaps were required.

### Duplicate Values

I also tested a list containing duplicate values:

[8, 3, 8, 2, 3, 1]

Both algorithms successfully sorted the list while preserving all duplicate values.

Sorted result:

[1, 2, 3, 3, 8, 8]

## Performance Comparison

Bubble Sort was simple to understand and implement because it repeatedly compared neighboring values and swapped values that were out of order. However, its O(n²) average and worst-case time complexity made it inefficient for large datasets.

Merge Sort used a divide-and-conquer strategy and had a time complexity of O(n log n). This made Merge Sort more appropriate for larger datasets where performance was important. The tradeoff was that Merge Sort required additional memory to divide and merge the lists.

For small or nearly sorted datasets, Bubble Sort could be useful because of its simplicity and early stopping optimization. For larger datasets, Merge Sort would generally provide better performance.

## Real-World Sorting Example

I created a streaming-platform example using content ratings:

[4.7, 3.9, 4.9, 4.2, 3.8, 4.5, 4.1]

Both Bubble Sort and Merge Sort organized the ratings as:

[3.8, 3.9, 4.1, 4.2, 4.5, 4.7, 4.9]

This demonstrated how sorting could be used by a streaming platform to organize content information before displaying movies or shows to users.

## Conclusion

This assignment helped me understand the differences between simple comparison-based sorting and divide-and-conquer sorting. I learned how Bubble Sort repeatedly compared adjacent values, while Merge Sort recursively divided data into smaller sections before merging the sorted results. Testing different datasets and edge cases also helped me understand why choosing the correct sorting algorithm is important when working with different amounts and types of data.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.