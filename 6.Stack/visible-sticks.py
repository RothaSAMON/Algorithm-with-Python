# from stack import Stack
# def solve(n, s):
#     stack = Stack()
#     for i in range(n):
#         while not stack.empty() and s[i] >= stack.peek():
#             stack.pop()
#         stack.push(s[i])
#     print(stack.stack)
#     return stack.size()

# N = int(input())
# S = list(map(int, input().split()))
# print(solve(N, S))

def solve(n, s):
    stack = []
    for i in range(n):
        while len(stack) > 0 and s[i] >= stack[-1]:
            stack.pop()
        stack.append(s[i])
    return len(stack)

N = int(input())
S = list(map(int, input().split()))
print(solve(N, S))