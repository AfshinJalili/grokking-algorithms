# Chapter 3: Recursion

This chapter introduces the concept of recursion and covers various recursive algorithms and techniques.

## 📚 Algorithms Implemented

### Recursive Binary Search (`binary-search.js`)
- **Purpose**: Binary search implemented using recursion (divide and conquer)
- **Time Complexity**: O(log n)
- **Space Complexity**: O(log n) due to call stack
- **Usage**: 
```javascript
const result = binarySearch([1, 3, 5, 7, 9], 3);
console.log(result); // Output: 1 (index of 3)
```

### Count Items (`count-items.js`)
- **Purpose**: Count the number of items in a list using recursion
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) due to call stack
- **Usage**: 
```javascript
const result = countItems([1, 2, 3, 4, 5]);
console.log(result); // Output: 5
```

### Find Maximum (`find-max.js`)
- **Purpose**: Find the maximum value in a list using recursion
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) due to call stack
- **Usage**: 
```javascript
const result = findMax([1, 5, 3, 9, 2]);
console.log(result); // Output: 9
```

### Recursive Sum (`sum.js`)
- **Purpose**: Calculate the sum of all numbers in a list using recursion
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) due to call stack
- **Usage**: 
```javascript
const result = sum([1, 2, 3, 4, 5]);
console.log(result); // Output: 15
```

## 🎯 Key Concepts from Chapter 3

### What is Recursion?
Recursion is a programming technique where a function calls itself to solve a problem. It's based on the principle of solving a problem by breaking it down into smaller, similar subproblems.

### Base Case and Recursive Case
Every recursive function has two parts:
1. **Base Case**: The simplest case that can be solved directly (stops the recursion)
2. **Recursive Case**: Breaks the problem into smaller subproblems and calls itself

### Divide and Conquer
Many recursive algorithms follow the divide and conquer pattern:
1. **Divide**: Break the problem into smaller subproblems
2. **Conquer**: Solve the subproblems recursively
3. **Combine**: Combine the solutions to solve the original problem

### Recursion vs Iteration
**Recursion:**
- More elegant and readable for certain problems
- Natural for tree/graph traversal
- Can lead to stack overflow for deep recursion
- Often more memory usage due to call stack

**Iteration:**
- Generally more memory efficient
- No risk of stack overflow
- Can be faster for simple problems
- May be less readable for complex logic

## 🚀 Running the Examples

```bash
# Run the recursive binary search example
bun run 3-recursion/binary-search.js

# Run the count items example
bun run 3-recursion/count-items.js

# Run the find maximum example
bun run 3-recursion/find-max.js

# Run the recursive sum example
bun run 3-recursion/sum.js
```

## 📖 Learning Notes

- Always ensure recursive functions have a base case to prevent infinite recursion
- Recursion is particularly useful for problems that can be naturally divided into smaller subproblems
- The call stack is crucial to understand when working with recursion
- Some problems are much easier to solve recursively than iteratively
- Recursion is the foundation for many advanced algorithms like tree traversal and dynamic programming

## 🔗 Related Resources

- [Recursion Visualization](https://visualgo.net/en/recursion) - Interactive visualization of recursion
- [Call Stack](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack) - Understanding how recursion uses the call stack
- [Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) - Algorithm design paradigm 