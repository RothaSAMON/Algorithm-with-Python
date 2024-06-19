def solve(n):
    sqrtn = int(n ** 0.5)
    cnt = 0

    for i in range(1, sqrtn + 1):
        if n % i == 0:
            cnt += 2

    if sqrtn * sqrtn == n:
        cnt -= 1
    return cnt

N = int(input())

import time 
start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time: {end - start}')
