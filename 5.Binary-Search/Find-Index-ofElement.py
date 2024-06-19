#Test Case :
# 8 7
# 11 17 26 28 37 45 53 59
# 33 28 64 53 81 26 11

#Output: -1 3 -1 6 -1 2 0 
# " -1 " it mean dont have and 0, 1, 2, ... it mean its index of position.

#Solution 1 :
# def binsearch(low, high, x, S):
#     if low > high:
#         return -1
#     else:
#         mid = (low + high) // 2
#         if x == S[mid]:
#             return mid
#         elif x < S[mid]:
#             return binsearch(low, mid - 1, x, S)
#         else: # x > s[mid]
#             return binsearch(mid + 1, high, x, S)
        
# def solve(n, m, S, X):
#     for i  in range(m):
#         j = binsearch(0, n - 1, X[i], S)
#         print(j, end = " ")
#     print()

# N, M = map(int, input().split())
# S = list(map(int, input().split()))
# X = list(map(int, input().split()))
# solve(N, M, S, X)


#Solution 2 :
def binsearch(x, n, S):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid
        elif x < S[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return -1

def solve(n, m, S, X):
    for i  in range(m):
        j = binsearch(X[i], n, S)
        print(j, end = " ")
    print()

N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)

