function insertionSort(n, s) {
    let cnt = 0;
    for (let i = 1; i < n; i++) {
        let j = i - 1;      //ex: j = 12 in array list
        let val = s[i];      //ex: val = 11 in the array list
        cnt += 1;
        
        while (j >= 0 && s[j] > val) {
            s[j + 1] = s[j];     //It mean if s[j] bigger than val : it will make shift
            j -= 1;       //j move to the previous position
            cnt += 1;
        //The loop continues until either j becomes less than 0 (meaning we have reached the beginning of the array),
        // or the value at index j is not greater than val (meaning we have found the correct position for val).
        }
        s[j + 1] = val;
    }
    return cnt;
}

const array = [23, 1, 10, 6, 2];
const length = array.length;

console.log("Input array:", array);
console.log("Number of comparisons:", insertionSort(length, array));
console.log("Sorted array:", array);
