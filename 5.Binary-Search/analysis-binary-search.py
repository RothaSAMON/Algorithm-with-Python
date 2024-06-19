# test case: ooutput: 21
# 8 7
# 11 17 26 28 37 45 53 59
# 33 28 64 53 81 26 11

#This is a iteration style:
# def binsearch(x, n, S):
#     low, high = 0, n - 1
#     cnt = 0
#     while low <= high:
#         mid = (low + high) // 2
#         cnt += 1
#         if x == S[mid]:
#             return cnt
#         elif x < S[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return cnt

# def solve(n, m, S, X):
#     total = 0
#     for i in range(m):
#         total += binsearch(X[i], n, S)
#     print(total)

# N, M = map(int, input().split())
# S = list(map(int, input().split()))
# X = list(map(int, input().split()))
# solve(N, M, S, X)






#this is a recursion style:
def binsearch(low, high, x, S):
    if low > high:
        return 0
    else:
        mid = (low + high)//2
        if x == S[mid]:
            return 1
        elif x < S[mid]:
            return 1 + binsearch(low, mid - 1, x, S)
        else:
            return 1 + binsearch(mid + 1, high, x, S)

def solve(n, m, S, X):
    total = 0
    for i in range(m):
        total += binsearch(0, n - 1, X[i], S)
    print(total)

N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
solve(N, M, S, X)