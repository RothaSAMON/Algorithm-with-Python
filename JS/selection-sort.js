function selectionsort(n, s) {
    let cnt = 0;
    for (let i = 0; i < n - 1; i++) {
        let minv = s[i];
        let minj = i;
        for (let j = i + 1; j < n; j++) {
            if (s[j] < minv) {
                minv = s[j];
                minj = j;
            }
        }
        if (i !== minj) {
            [s[i], s[minj]] = [s[minj], s[i]];
            
            cnt++;
        }
    }
    return cnt;
}

const input = require('readline-sync');

const N = parseInt(input.question("Enter the number of elements: "));
const S = input.question("Enter the elements separated by spaces: ").split(' ').map(Number);

console.log(selectionsort(N, S));
