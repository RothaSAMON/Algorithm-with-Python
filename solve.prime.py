def solve(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

N = int(input())
print("YES" if solve(N) else "NO")

import time
start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time: {end - start}')