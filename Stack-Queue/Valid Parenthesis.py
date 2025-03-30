# Function to check if the string is valid
def isValidParenthesis(s):
    stack = []  # Create an empty stack

    # Loop through each character in the string
    for char in s:
        if char == '(':  # If opening bracket, push to stack
            stack.append(char)
        elif char == ')':  # If closing bracket
            if not stack:  # If stack is empty, no matching opening bracket
                return 0
            stack.pop()  # Remove last opening bracket from stack    

    # If stack is empty, all brackets are matched
    return 1 if not stack else 0

# Input number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    S = input().strip()
    print(isValidParenthesis(S))

