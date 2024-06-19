def seqsearch(x, n, S):
    for i in range(n):
        if x == S[i]:
            return i
    return -1

def solve(n, m, S, X): 
    for i in range(m):
        print(seqsearch(X[i], n, S), end=" ")

N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)
# This code is about to Search for the index (X to search num of if it have in S or not)
# Its output the index if the position  of it have, else it output -1