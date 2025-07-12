function findSmallest(arr) {
  let smallest = arr[0];
  let smallestIndex;
  arr.forEach((element, index) => {
    if (element < smallest) {
      smallest = element;
      smallestIndex = index;
    }
  });
  return smallestIndex;
}

function selectionSort(arr) {
  const sortedArr = [];
  const copiedArr = Array.from(arr);
  for (let i = 0; i < arr.length; i++) {
    const smallestIndex = findSmallest(copiedArr);
    sortedArr.push(...copiedArr.splice(smallestIndex, 1));
  }
  return sortedArr;
}

console.log(selectionSort([5, 3, 6, 2, 10]));
