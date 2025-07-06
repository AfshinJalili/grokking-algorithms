# Chapter 1: Introduction to Algorithms

This chapter covers the fundamental concepts of algorithms and introduces the first algorithm: Binary Search.

## 📚 Algorithms Implemented

### Binary Search (`binary-search.js`)
- **Purpose**: Efficiently find an element in a sorted array
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Usage**: 
```javascript
const result = binarySearch([1, 3, 5, 7, 9], 3);
console.log(result); // Output: 1 (index of 3)
```

## 🎯 Key Concepts from Chapter 1

### What is an Algorithm?
An algorithm is a set of instructions for accomplishing a task. Every piece of code could be called an algorithm, but this book focuses on algorithms that solve specific problems.

### Binary Search
Binary search is an algorithm that runs in logarithmic time. It's much faster than simple search, especially for large lists.

**How it works:**
1. Start with a sorted list
2. Check the middle element
3. If the target is found, return the position
4. If the target is less than the middle, search the lower half
5. If the target is greater than the middle, search the upper half
6. Repeat until the target is found or the search space is empty

**Why it's efficient:**
- Each step eliminates half of the remaining elements
- Time complexity: O(log n) instead of O(n) for simple search
- Perfect for large datasets

## 🚀 Running the Examples

```bash
# Run the binary search example
bun run ch1/binary-search.js
```

## 📖 Learning Notes

- Binary search only works on sorted lists
- The "guess and check" approach is much more efficient than checking every element
- Understanding logarithmic time complexity is crucial for algorithm analysis
- This chapter sets the foundation for understanding algorithm efficiency

## 🔗 Related Resources

- [Binary Search Visualization](https://visualgo.net/en/bst) - Interactive visualization of binary search
- [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation) - Understanding time complexity 