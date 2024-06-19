# def evaluate_postfix(expression):
#     stack = []
    
#     for token in expression.split():
#         if token.isdigit():
#             stack.append(int(token))
#         else:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
            
#             if token == '+':
#                 stack.append(operand1 + operand2)
#             elif token == '-':
#                 stack.append(operand1 - operand2)
#             elif token == '*':
#                 stack.append(operand1 * operand2)
#             elif token == '/':
#                 stack.append(operand1 / operand2)
#             else:
#                 raise ValueError(f"Unknown operator: {token}")
    
#     return stack.pop()

# postfix_expression = "2 3 4 * +"
# print('output is:', evaluate_postfix(postfix_expression))


#AnB Code
def solve(X):
    stack = []
    for x in X:
        if x.isdigit():
            stack.append(int(x))
        else:
            b, a = stack.pop(), stack.pop()
            if x == '+': stack.append(a + b)
            elif x == '-': stack.append(a - b)
            elif x == '*': stack.append(a * b)
            elif x == '/': stack.append(a // b)
    return stack[-1]
X = input()
print(solve(X))