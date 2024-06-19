# test case:
# 7
# 18 27 42 82 73 67 25

# output: 3 82 (it mean 3 is the index of the value 82)

#This is a recusion  :
# def binsearch(low, high, n, s):
#     mid = (low + high) // 2
#     if  mid == 0 or mid > (n - 1):
#         return -1
#     else:
#         if s[mid - 1] < s[mid] > s[mid + 1]:
#             return mid
#         elif s[mid - 1] < s[mid] < s[mid + 1]:
#             return binsearch(mid + 1, high, n, s)
#         else:
#             return binsearch(low, mid - 1, n, s)
        
# def solve(n, s):
#     j = binsearch(0, n - 1, n, s)
#     print(j, s[j])
# N = int(input())
# S = list(map(int, input().split()))
# solve(N, S)


#This is a iteration:
def binsearch(n, s):
    low, high = 0, n - 1
    mid = (low + high) // 2
    while mid != 0 and mid != n - 1:
        mid = (low + high) // 2
        if s[mid - 1] < s[mid] > s[mid + 1]:
            return mid
        elif s[mid - 1] < s[mid] < s[mid+ 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def solve(n, s):
    j = binsearch(n, s)
    print(j, s[j])
N = int(input())
S = list(map(int, input().split()))
solve(N, S)