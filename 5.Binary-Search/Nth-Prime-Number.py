"""
This is MINE:

def is_prime(n):
    #Check if a number is prime.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


input_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# Identify primes in the input list
primes = [num for num in input_numbers if is_prime(num)]


# Generate output list
results = []
for num in input_numbers:
    if is_prime(num):
        # Get the 1-based index of the prime number in the primes list
        index = primes.index(num) + 1
        results.append(index)
    else:
        results.append(0)

print("Output:", " ".join(map(str, results)))
"""

#This number is to find the Nth prime number:
#It will output 0 if its not prime, else its output from order of the number 1, 2, 3, ...
#TEST CASE:
#10
#1 2 3 4 5 6 7 8 11 13
#OUTPUT: 0 1 2 0 3 0 4 0 5 6 


#This is a iteration:
def find_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i] == 1]

def binsearch(x, n, s):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def solve(n, s, maxn):
    primes = find_primes(maxn)
    for i in range(n):
        j = binsearch(s[i], len(primes), primes)
        print(j + 1, end = " ")
    print()

N = int(input())
S = list(map(int, input().split()))
solve(N, S, 100000)

"""
#This is a code with the meaningful variable:

def find_primes(limit):
    #Find all prime numbers up to a given limit using the Sieve of Eratosthenes.
    # Initialize a list to mark prime numbers
    sieve = [0, 0] + [1] * (limit - 1)  # 0 and 1 are not primes, so mark them as 0
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num] == 1:  # If num is a prime
            # Mark multiples of num as non-prime
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = 0
    # Return the list of primes
    return [num for num in range(limit + 1) if sieve[num] == 1]

def binary_search(target, array_length, array):
    #Perform binary search to find the index of target in sorted array.
    low, high = 0, array_length - 1
    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Return -1 if the target is not found

def solve(num_count, num_list, max_limit):
    #Solve the problem by finding primes and their indices in the input list.
    primes = find_primes(max_limit)
    for i in range(num_count):
        index = binary_search(num_list[i], len(primes), primes)
        # Output the 1-based index of the prime, or 0 if not prime
        print(index + 1 if index != -1 else 0, end=" ")
    print()

# Read input values
N = int(input("Enter the number of elements: "))
S = list(map(int, input("Enter the elements separated by spaces: ").split()))
# Solve the problem with the given input and a maximum limit for prime search
solve(N, S, 100000)

"""

#This is a Recursive:

def binsearch(low, high, x, s):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if x == s[mid]:
            return mid
        elif x < s[mid]:
            return binsearch(low, mid - 1, x, s)
        else:
            return binsearch(mid + 1, high, x, s)
        
def solve(n, s, maxn):
    primes = find_primes(maxn)
    for i in range(n):
        j = binsearch(0, len(primes) - 1, s[i], primes)
        print(j + 1, end= " ")
    print()

def fins_primes(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i] == 1]

N = int(input("Input the number of elements: "))
S = list(map(int, input("Input the numbers separated by spaces: ").split()))
solve(N, S, 100000)