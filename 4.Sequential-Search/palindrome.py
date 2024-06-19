def is_palindrome(n):
    r, m = 0, n
    while m > 0:
        r *= 10
        r += m % 10
        m //= 10
    return n == r

def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if is_palindrome(i):
            cnt += 1
    return cnt

N, M = map(int, input().split())
print(solve(N, M))


#TEST CASE: input: 100 1000 input: 1 100000 input: 10 100


#In here is another style to find the palindrome :

# def is_palindrome(n):
#     s = str(n)
#     r = s[::-1]
#     return int(s) == int(r)

# def solve(n, m):
#     cnt = 0
#     for i in range(n, m + 1):
#         if is_palindrome(i):
#             cnt += 1
#     return cnt
# N, M = map(int, input().split())
# print(solve(N, M))