
#TEST CASE: 
#4 6
#20 15 10 17
#OUTPUT: 15


#This is a recursive
# def binsearch(low, high, n, M, s):
#     if low >= high:
#         return low - 1
#     else:
#         mid = (low + high) // 2
#         if cut(n, s, mid) < M:
#             return binsearch(low, mid, n, M, s)
#         else:
#             return binsearch(mid + 1, high, n, M, s)
        
# def cut(n, s, h):
#     length = 0
#     for i in range(n):
#         length += (s[i] - h) if s[i] > h else 0
#     return length

# def solve(n, M, s):
#     j = binsearch(0, max(s), n, M, s)
#     print(j)

# N, M = map(int, input().split())
# S = list(map(int, input().split()))

# solve(N, M, S)



#This is a iteration: intermediate
def binsearch(n, M, s):
    low, high = 0, max(s)
    while low < high:
        mid = (low + high) // 2
        if cut(n, s, mid) < M:
            high = mid
        else:
            low = mid + 1
    return low - 1

def cut(n, s, h):
    length = 0
    for i in range(n):
        length += (s[i] - h) if s[i] > h else 0
    return length

def solve(n, M, s):
    j = binsearch(n, M, s)
    print(j)

N, M = map(int, input().split())
S = list(map(int, input().split()))
solve(N, M, S)