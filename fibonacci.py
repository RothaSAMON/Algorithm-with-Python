# def fibonacci(n):
#     fib_sequence = [0, 1]

#     for i in range(2, n):
#         next_number = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_number)

#     return fib_sequence

# n = 10000
# print(f"Fibonacci sequence up to {n}:", fibonacci(n))

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
N = int(input())
print(fib(N))