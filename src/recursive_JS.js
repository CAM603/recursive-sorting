// MERGE SORT
// It is useful to first implement a function responsible for merging two sorted arrays
// Given two arrays which are sorted, a helper function shhould create a new array which is also sorted, and consist of all the elements in the two input arrays
// This function should run in O(n + m) time and space and should not modify the parameters passed to it

function merge(arr1, arr2) {
    let results = [];
    let i = 0;
    let j = 0;
    // while i is less than length of array and j is less than length of array
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            results.push(arr1[i]);
            i++;
        } else {
            results.push(arr2[j]);
            j++;
        }
    }
    while (i < arr1.length) {
        results.push(arr1[i]);
        i++;
    }
    while (j < arr2.length) {
        results.push(arr2[j]);
        j++;
    }

    return results;
}
// arrA = [1, 3, 5, 7, 9];
// arrB = [2, 4, 6, 8];
// console.log(merge(arrA, arrB));

function mergeSort(arr) {
    let mid = Math.floor(arr.length / 2);
    let left = arr.slice(0, mid);
    let right = arr.slice(mid);
    if (arr.length > 1) {
        left = mergeSort(left);
        right = mergeSort(right);
        return merge(left, right);
    }
    return arr;
}
let myArr = [1, 3, 5, 7, 9, 2, 4, 6, 8];
console.log(mergeSort(myArr));
