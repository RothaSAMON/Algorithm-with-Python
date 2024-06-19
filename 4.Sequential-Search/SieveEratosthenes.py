
#This is a step 1 and the calculate is a bit slow than step2 cuz we didnt use root :
# def find_primes(n):
#     sieve = [0, 0] + [1] * (n - 1)
#     for i in range(2, n + 1):
#         if sieve[i] == 1:
#             for j in range(i + i, n + 1, i):
#                 sieve[j] = 0
#     return sieve

# def solve(n):
#     sieve = find_primes(n)
#     return sum(sieve)

# N = int(input())
# print(solve(N))


#This is a step 2 and the calculate is a bit faster than step1 cuz we did use root :
def find_primes(n):
    # Step 1: Create a list where index represents the number, and value is 1 (prime) or 0 (not prime)
    sieve = [0, 0] + [1] * (n - 1)  # 0 and 1 are not primes, rest are assumed to be prime initially

    # Step 2: Iterate over each number starting from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:  # Check if the number is still marked as prime
            # Step 3: Mark all multiples of i as not prime
            for j in range(i * i, n + 1, i):
                sieve[j] = 0  # Mark multiples of i as not prime

    return sieve  # Return the list with prime status

def solve(n):
    sieve = find_primes(n)  # Get the list of prime statuses
    return sum(sieve)  # Sum the list to count the number of primes

# Main part of the code
N = int(input("Enter a number: "))  # Read input from the user
print(solve(N))  # Print the number of primes up to N
