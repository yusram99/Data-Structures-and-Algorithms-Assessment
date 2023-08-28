# Question 1: Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

# An expression is considered balanced if each opening bracket has a corresponding closing 
# bracket in the correct order.

# sample input = 

# expression1 = "([]{})"
# expression2 = "([)]"
# print(is_balanced(expression1))  # Output: True
# print(is_balanced(expression2))  # Output: False 

def is_balanced(expression):
    # Stack to hold the brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    # Set of opening brackets
    opening_brackets = set(['(', '{', '['])
    
    # Traverse through the expression
    for bracket in expression:
        # If it's an opening bracket, push at the stack
        if bracket in opening_brackets:
            stack.append(bracket)
        elif stack and brackets_map[bracket] == stack[-1]:
            # If it's a closing bracket, check the top element of stack
            # If it matches, pop the top element from stack
            stack.pop()
        else:
            # If it's a closing bracket and doesn't match the top element of stack
            return False

    # The stack should be empty at the end
    return not stack
# Tests
sampleinput = []
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False