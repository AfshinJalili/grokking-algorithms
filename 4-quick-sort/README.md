# Chapter 4: Quick Sort

This chapter covers Quick Sort, a highly efficient sorting algorithm that uses the divide and conquer strategy.

## 📚 Algorithms Implemented

### Quick Sort (`quick-sort.js`)
- **Purpose**: Sort an array using the quick sort algorithm (divide and conquer)
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n) average due to call stack
- **Usage**: 
```javascript
const result = quickSort([5, 3, 6, 2, 10]);
console.log(result); // Output: [2, 3, 5, 6, 10]
```

## 🎯 Key Concepts from Chapter 4

### What is Quick Sort?
Quick sort is a highly efficient, comparison-based sorting algorithm that uses the divide and conquer strategy. It works by selecting a 'pivot' element and partitioning the other elements into two subarrays according to whether they are less than or greater than the pivot.

### How Quick Sort Works
1. **Choose a pivot**: Select an element from the array (often the last element)
2. **Partition**: Rearrange the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it
3. **Recurse**: Apply the same steps to the subarrays on either side of the pivot
4. **Combine**: The subarrays are already sorted, so no combining step is needed

### Pivot Selection Strategies
- **Last element**: Simple but can lead to poor performance on already sorted arrays
- **First element**: Also simple but can have similar issues
- **Middle element**: Often provides good balance
- **Random element**: Provides good average-case performance
- **Median-of-three**: Choose the median of first, middle, and last elements

### Time Complexity Analysis
- **Best Case**: O(n log n) - When pivot divides array roughly in half
- **Average Case**: O(n log n) - Typical performance with good pivot selection
- **Worst Case**: O(n²) - When pivot is always the smallest or largest element
- **Space Complexity**: O(log n) - Due to recursive call stack

### Why Quick Sort?
**Advantages:**
- Excellent average-case performance (O(n log n))
- In-place sorting (minimal extra memory)
- Cache-friendly due to good locality of reference
- Widely used in practice (many programming language standard libraries)

**Disadvantages:**
- Unstable sort (equal elements may change relative order)
- Poor performance on already sorted or reverse-sorted arrays
- Worst-case O(n²) time complexity
- Recursive nature can lead to stack overflow for very large arrays

## 🚀 Running the Examples

```bash
# Run the quick sort example
bun run 4-quick-sort/quick-sort.js
```

## 📖 Learning Notes

- Quick sort is often faster in practice than other O(n log n) algorithms like merge sort
- The choice of pivot is crucial for performance
- Quick sort demonstrates the power of divide and conquer strategy
- Understanding the partitioning step is key to understanding quick sort
- The algorithm is "quick" because it sorts in-place and has good cache performance

## 🔗 Related Resources

- [Quick Sort Visualization](https://visualgo.net/en/sorting) - Interactive visualization of quick sort
- [Sorting Algorithm Comparison](https://www.toptal.com/developers/sorting-algorithms) - Compare different sorting algorithms
- [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) - Algorithm design paradigm 