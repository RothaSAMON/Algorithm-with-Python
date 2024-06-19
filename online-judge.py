import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(N, M):
    primes = []
    for num in range(max(N, 2), M + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    N = int(input("Enter the lower bound (N): "))
    M = int(input("Enter the upper bound (M): "))
    
    prime_numbers = find_primes(N, M)
    if len(prime_numbers) == 0:
        print("There are no prime numbers in the specified range.")
    else:
        prime_numbers.sort()
        print("The last 5 largest prime numbers between", N, "and", M, "are:")
        for prime in prime_numbers[-5:]:
            print(prime)

if __name__ == "__main__":
    main()
