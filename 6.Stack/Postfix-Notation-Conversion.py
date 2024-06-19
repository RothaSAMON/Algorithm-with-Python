# precedence = {'(':0, ')':1, '+':2, '-':2, '*':3, '/':3}

# def solve(X):
#     stack, postfix = [], ""
#     for x in X:
#         if x.isalpha(): postfix += x
#         elif x == '(': stack.append(x)
#         else:
#             while stack and precedence[x] <= precedence[stack[-1]]:
#                 postfix += stack.pop()
#             if x == ')': stack.pop() #remove '('
#             else: stack.append(x) #operator
#     while stack:
#         postfix += stack.pop()
#     return postfix

# X = input()
# print(solve(X))




# Dictionary to store the precedence of operators
precedence = {'(': 0, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}

def infix_to_postfix(expression):
    operator_stack = []  # Stack to keep operators
    postfix_expression = ""  # Resultant postfix expression
    
    for char in expression:
        if char.isalpha():  # If the character is an operand, add it to postfix expression
            postfix_expression += char
        elif char == '(':  # If the character is '(', push it to the stack
            operator_stack.append(char)
        elif char == ')':  # If the character is ')', pop from the stack until '(' is encountered
            while operator_stack and operator_stack[-1] != '(':
                postfix_expression += operator_stack.pop()
            operator_stack.pop()  # Remove '(' from stack
        else:  # The character is an operator
            while operator_stack and precedence[char] <= precedence[operator_stack[-1]] and operator_stack[-1] != '(':
                postfix_expression += operator_stack.pop()
            operator_stack.append(char)  # Push the current operator to the stack

    # Pop all the operators from the stack
    while operator_stack:
        postfix_expression += operator_stack.pop()

    return postfix_expression

# Read input from user
expression = input("Enter infix expression: ")
# Convert infix to postfix and print the result
print(infix_to_postfix(expression))
