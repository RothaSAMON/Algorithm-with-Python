def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = 48
num2 = 18
print(gcd(num1, num2))