#Test case :
# 9 = 3
# 15 = 7
# 123 = 331
# 1234 = 31724 (long time)
# 12345 = 3176523

#With is cant be calculate the big number :
# def solve(n):
#     cnt = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range(b, n):
#                 if a + b + c == n and a + b > c:
#                     cnt += 1
#     return cnt

# N = int(input())
# print(solve(N))


#Now this is a improvement but it still take a long time :
#Stratergy 1
# def solve(n):
#     cnt = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             c = n - a - b
#             if b <= c and a + b > c:
#                 cnt += 1
#     return cnt
# N = int(input())
# print(solve(N))


#With this it can test6 but to long time . . .
#Stratergy 2
# def solve(n):
#     cnt = 0
#     for c in range((n + 1) // 3, (n + 1) // 2):
#         for b in range((n - c + 1) // 2, c + 1):
#             cnt += 1
#     return cnt

# N = int(input())
# print(solve(N))


#this is a last improvement and calculate all
#Stratergy 3
def solve(n):
    cnt = 0
    for c in range((n + 1) // 3, (n + 1) // 2):
        cnt += c - (n - c + 1) // 2 + 1
    return cnt

N = int(input())
print(solve(N))