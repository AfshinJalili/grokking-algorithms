function countItems(arr) {
  if (arr[0] === undefined) {
    return 0;
  }
  return 1 + countItems(arr.slice(1));
}

console.log(countItems([1, 2, 3, 4, 5]));
