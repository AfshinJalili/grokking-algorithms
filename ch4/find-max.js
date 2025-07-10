function findMax(arr) {
  if (arr.length === 1) {
    return arr[0];
  } else {
    return Math.max(arr[0], findMax(arr.slice(1)));
  }
}

console.log(findMax([0, 6, 3, 4, 5]));
