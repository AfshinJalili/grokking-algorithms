function sum(arr) {
  if (arr.length === 1) {
    return arr[0];
  } else {
    return arr[0] + sum(arr.splice(1));
  }
}

console.log(sum([1, 2, 3, 4, 5, 6]));

