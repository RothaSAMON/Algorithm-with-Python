#This is t check the number between which is Prime and Palindrome: If the number
# are true in those two condition so output the count of it. Ex: N = 10 M = 100 OUTPUT: 1 
# Note: The prime and palindrome number of 10 -> 100 is 11. Only one in there.


def is_prme(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)

#Solution 1 : This a bit slow than solution 2
# def solve(n, m):
#     cnt = 0
#     for i in range(n, m + 1):
#         if is_prme(i) and is_palindrome(i):
#             cnt += 1
#     return cnt
# N, M = map(int, input().split())
# print(solve(N, M))

#Solution 2
def solve(n, m):
    cnt = 0
    for i in range(n, m + 1):
        if is_palindrome(i) and is_prme(i): #We reverse the position of function to perform faster
            cnt += 1
    return cnt
N, M = map(int, input().split())
print(solve(N, M))


import time
start = time.time()
solve(N, M)
end = time.time()
print(f"solve1() elapsed time = {end - start}")