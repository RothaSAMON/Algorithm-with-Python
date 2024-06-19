#Test case:
# 1 100
# 2022

# output:
# Bigger than 50? Yes.
# Bigger than 75? No.
# Bigger than 63? Yes.
# Bigger than 69? No.
# Bigger than 66? Yes.
# Bigger than 68? Yes.
# Your X is 69.


#This is a solution 1 :

# def solve(x, s, t):
#     low, high = s, t
#     while low < high:
#         mid = (low + high) // 2
#         print(f"Bigger than {mid}?", end=" ")
#         if x > mid:
#             print("Yes.")
#             low = mid + 1
#         else:
#             print("No.")
#             high = mid
#     print(f"Your X is {low}.")
#     return low

# import random
# S, T = map(int, input().split())
# SEED = int(input())
# random.seed(SEED)
# X = random.randint(S, T)
# solve(X, S, T)




# this is a solution 2: recursion

def solve(x, low, high):
    if low >= high:
        print(f"Your X is {low}.")
        return low
    else:
        mid = (low + high) // 2
        print(f"Bigger than {mid}?", end = " ")
        if x > mid:
            print("Yes.")
            return solve(x, mid + 1, high)
        else:
            print("No.")
            return solve(x, low, mid)
        
import random
S, T = map(int, input().split())
SEED = int(input())
random.seed(random.seed(SEED))
print(random)
X = random.randint(S, T)
solve(X, S, T)