function seqsearch(x, n, S) {
    for (let i = 0; i < n; i++) {
        if (x === S[i]) {
            return i;
        }
    }
    return -1;
}

function solve(n, m, S, X) {
    let result = [];
    for (let i = 0; i < m; i++) {
        result.push(seqsearch(X[i], n, S));
    }
    console.log(result.join(" "));
}

// Input
const N = 5;
const M = 3;
const S = [1, 2, 3, 4, 5];
const X = [3, 7, 5];

// Call the solve function
solve(N, M, S, X);
