//CountZeros

function countZeroes(arr) {
  let firstZero = findFirst(arr);
  if (firstZero === -1) {
    return 0;
  }

  count = arr.length - firstZero;
  return count;
}

function findFirst(arr) {
  leftIdx = 0;
  rightIdx = arr.length - 1;
  while (leftIdx <= rightIdx) {
    let midIdx = Math.floor((rightIdx + leftIdx) / 2);
    let midVal = arr[midIdx];
    if ((midVal === 0 && arr[midIdx - 1] === 1) || midIdx === 0) {
      return midIdx;
    } else if (midVal === 1) {
      leftIdx = midIdx + 1;
    } else {
      rightIdx = midIdx - 1;
    }
  }
  return -1;
}

// sortedFrequency

function findFirstSorted(arr, num) {
  leftIdx = 0;
  rightIdx = arr.length - 1;
  while (leftIdx <= rightIdx) {
    let midIdx = Math.floor((leftIdx + rightIdx) / 2);
    let midVal = arr[midIdx];
    if (midIdx === 0 || (num === midVal && num > arr[midIdx - 1])) {
      return midIdx;
    } else if (num > midVal) {
      leftIdx = midIdx + 1;
    } else {
      rightIdx = midIdx - 1;
    }
  }
  return -1;
}

function findLastSorted(arr, num) {
  leftIdx = 0;
  rightIdx = arr.length - 1;
  while (leftIdx <= rightIdx) {
    let midIdx = Math.floor((leftIdx + rightIdx) / 2);
    let midVal = arr[midIdx];
    if (
      (num === midVal && num < arr[midIdx + 1]) ||
      midIdx === arr.length - 1
    ) {
      return midIdx;
    } else if (num < midVal) {
      rightIdx = midIdx - 1;
    } else {
      leftIdx = midIdx + 1;
    }
  }
  return -1;
}

function findSortedFrequency(arr, num) {
  let firstIdx = findFirstSorted(arr, num);
  let lastIdx = findLastSorted(arr, num);
  return lastIdx - firstIdx + 1;
}

// findRotatedIndex

function findRotatedIndex(arr, num) {
  let pivot = findPivot(arr);
  if (arr[pivot] === num) {
    return pivot;
  } else if (num > arr[pivot] && num < arr[arr.length - 1]) {
    leftIdx = pivot;
    rightIdx = arr.length - 1;
  } else {
    leftIdx = 0;
    rightIdx = pivot;
  }
  while (leftIdx <= rightIdx) {
    console.log(leftIdx, rightIdx);
    let midIdx = Math.floor((leftIdx + rightIdx) / 2);
    let midVal = arr[midIdx];
    if (midVal === num) {
      return midIdx;
    } else if (num < midVal) {
      rightIdx = midIdx - 1;
    } else {
      leftIdx = midIdx + 1;
    }
  }
  return -1;
}

function findPivot(arr) {
  let leftIdx = 0;
  let rightIdx = arr.length - 1;
  while (leftIdx <= rightIdx) {
    let mid = Math.floor((leftIdx + rightIdx) / 2);
    if (arr[mid] > arr[mid + 1]) return mid + 1;
    else if (arr[leftIdx] <= arr[mid]) {
      leftIdx = mid + 1;
    } else {
      rightIdx = mid - 1;
    }
  }
}

// findFloor
function findFloor(arr, num) {
  leftIdx = 0;
  rightIdx = arr.length - 1;
  if (num >= arr[rightIdx]) return arr[rightIdx];
  while (leftIdx <= rightIdx) {
    let midIdx = Math.floor((leftIdx + rightIdx) / 2);
    let midVal = arr[midIdx];

    if ((midVal < num && arr[midIdx + 1] > num) || midVal === num) {
      return midVal;
    } else if (num < midVal) {
      rightIdx = midIdx - 1;
    } else {
      leftIdx = midIdx + 1;
    }
  }

  return -1;
}
