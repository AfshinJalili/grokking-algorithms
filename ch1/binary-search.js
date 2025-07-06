function binarySearch(arr, target) {
    let low = 0
    let high = arr.length - 1

    while (low <= high) {
        const mid = Math.floor((high + low) / 2)
        const guess = arr[mid]
        if (guess === target) {
          return mid;
        } else if (guess < target) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
    }

    return null
}

console.log(binarySearch([1,3,5,7,9], 3))