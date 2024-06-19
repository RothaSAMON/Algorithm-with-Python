# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping.keys():
#             if stack == [] or mapping[char] != stack.pop():
#                 return "No"
#         else:
#             continue #If the character is not a parenthesis, skip it
    
#     return "Yes" if stack == [] else "No"

# input_string = input()
# print(is_valid_parentheses(input_string))


#AnB Code
def solve(S):
    opening = "[{("
    closing = "]})"
    stack = []
    for s in S:
        if s in opening:
            stack.append(s)
        elif stack and opening.index(stack[-1]) == closing.index(s):
            stack.pop()
        else:
            return False
    return len(stack) == 0
S = input()
print("Yes" if solve(S) else "No")