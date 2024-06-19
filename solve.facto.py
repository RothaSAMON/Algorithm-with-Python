# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
# n = 1000
# print(fact(n))

def facto(n):
    facto_res = 1
    if n == 0:
        facto_res = 1
    else:
        for i in range(1, n + 1):
            facto_res *= i
    return facto_res
n = 1000
print(facto(n))
