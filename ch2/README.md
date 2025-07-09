# Chapter 2: Selection Sort

This chapter introduces the concept of sorting algorithms and covers Selection Sort, one of the fundamental sorting algorithms.

## 📚 Algorithms Implemented

### Selection Sort (`selection-sort.js`)
- **Purpose**: Sort an array by repeatedly finding the minimum element and placing it at the beginning
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Usage**: 
```javascript
const result = selectionSort([5, 3, 6, 2, 10]);
console.log(result); // Output: [2, 3, 5, 6, 10]
```

## 🎯 Key Concepts from Chapter 2

### What is Selection Sort?
Selection sort is a simple sorting algorithm that works by dividing the input into a sorted and unsorted region. The algorithm repeatedly selects the smallest element from the unsorted region and moves it to the end of the sorted region.

### How Selection Sort Works
1. Find the smallest element in the unsorted array
2. Swap it with the first element of the unsorted array
3. Move the boundary between sorted and unsorted arrays one element to the right
4. Repeat until no unsorted elements remain

**Step-by-step example with [5, 3, 6, 2, 10]:**
- **Pass 1**: Find smallest (2), swap with first element → [2, 3, 6, 5, 10]
- **Pass 2**: Find smallest in remaining (3), already in place → [2, 3, 6, 5, 10]
- **Pass 3**: Find smallest in remaining (5), swap with 6 → [2, 3, 5, 6, 10]
- **Pass 4**: Find smallest in remaining (6), already in place → [2, 3, 5, 6, 10]
- **Pass 5**: Find smallest in remaining (10), already in place → [2, 3, 5, 6, 10]

### Time Complexity Analysis
- **Best Case**: O(n²) - Even if array is sorted, we still need to check all elements
- **Average Case**: O(n²) - Typical performance
- **Worst Case**: O(n²) - When array is reverse sorted
- **Space Complexity**: O(1) - In-place sorting algorithm

### Why Selection Sort?
**Advantages:**
- Simple to understand and implement
- Performs well on small lists
- Minimal memory usage (in-place sorting)
- Good for educational purposes

**Disadvantages:**
- Poor performance on large datasets
- O(n²) time complexity makes it inefficient for large arrays
- Not stable (equal elements may change relative order)

## 🚀 Running the Examples

```bash
# Run the selection sort example
bun run ch2/selection-sort.js
```

## 📖 Learning Notes

- Selection sort is a good starting point for understanding sorting algorithms
- The algorithm demonstrates the concept of "divide and conquer" by separating sorted and unsorted regions
- Understanding why it's O(n²) helps build intuition for algorithm analysis
- This chapter introduces the concept of comparing algorithms based on their efficiency
- Selection sort is rarely used in practice due to its poor performance, but it's excellent for learning

## 🔗 Related Resources

- [Selection Sort Visualization](https://visualgo.net/en/sorting) - Interactive visualization of selection sort
- [Sorting Algorithm Comparison](https://www.toptal.com/developers/sorting-algorithms) - Compare different sorting algorithms
- [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation) - Understanding time complexity 