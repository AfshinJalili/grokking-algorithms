function binarySearch(arr, target) {
  // Base case 1: Empty array - target not found
  if (arr.length === 0) {
    return null;
  }

  // Base case 2: Single element array - check if it's the target
  if (arr.length === 1) {
    return arr[0] === target ? 0 : null;
  }

  // Recursive case: Divide and conquer
  const mid = Math.floor(arr.length / 2);
  const midValue = arr[mid];

  if (midValue === target) {
    return mid; // Found the target
  } else if (midValue < target) {
    // Search the right half
    const rightResult = binarySearch(arr.slice(mid + 1), target);
    return rightResult !== null ? mid + 1 + rightResult : null;
  } else {
    // Search the left half
    return binarySearch(arr.slice(0, mid), target);
  }
}

console.log(binarySearch([1, 3, 5, 7, 9], 3)); // Should return 1
console.log(binarySearch([1, 3, 5, 7, 9], 9)); // Should return 4
console.log(binarySearch([1, 3, 5, 7, 9], 2)); // Should return null
