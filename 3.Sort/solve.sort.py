# import random
# SEED, MIN, MAX, N = 2022, 10, 100, 8
# random.seed(SEED)
# S = random.sample(range(MIN, MAX), N)

# print(S)
# print(sorted(S))


def solve(n, s):
    odd, even = [], []
    for i in range(n):
        if s[i] % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    odd.sort()
    even.sort(reverse= True)

    print(" ".join(map(str, odd)))
    print(" ".join(map(str, even)))

N = int(input())
S = list(map(int, input().split()))
solve(N, S)