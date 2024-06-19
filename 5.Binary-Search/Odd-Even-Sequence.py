#This find the first even num appear first and if no even its print 0
# TEST Case:
# 1:         8
#            7 3 1 9 8 4 2 6
#Output:     8   

# 2:         10
#            69 19 97 36 52 24 82 10 34 44
#Output:     36 

# 3:         7
#            11 67 33 55 83 47 29
#Output:     0 



# MINE :
# def find_first_even_number(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             return number
#     return 0

# N = int(input())
# numbers = list(map(int, input().split()))

# result = find_first_even_number(numbers)
# print(result)



# AnB :

#Solution 1 : Recursion function
# def  binsearch(low, high, n, s):
#     if low == high:
#         return -1 if s[low] % 2 == 1 else low
#     else:
#         mid = (low + high) // 2
#         if s[mid] % 2 == 0:
#             return binsearch(low, mid, n, s)
#         else:
#             return binsearch(mid + 1, high, n, s)
        
# def solve(n, s):
#     j = binsearch(0, n - 1, n, s)
#     print(0 if j < 0 else s[j])
# N = int(input())
# S = list(map(int, input().split()))
# solve(N, S)


#Solution 2 : Iteration function
def binsearch(n, s):
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if s[mid] % 2 == 0:
            high = mid
        else:
            low = mid + 1

    return -1 if s[low] % 2 == 1 else low

def solve(n, s):
    j = binsearch(n, s)
    print(0 if j < 0 else s[j])
N = int(input())
S = list(map(int, input().split()))
solve(N, S)