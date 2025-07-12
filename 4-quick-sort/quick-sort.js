function quickSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const pivot = arr[0];
  const less = [];
  const greater = [];
  for (let i = 1; i < arr.length; i++) {
    arr[i] > pivot ? greater.push(arr[i]) : less.push(arr[i]);
  }
  return [...quickSort(less), pivot, ...quickSort(greater)];
}

console.log(quickSort([10, 5, 2, 3]));
