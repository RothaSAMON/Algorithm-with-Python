def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

num = 2
print(len(collatz(num)))
import time 
start = time.time()
print(collatz(num))
end = time.time()
print(f'solve() elapsed time: {end - start}')