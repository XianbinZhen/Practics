# You are given a string of parenthesis.
# Return the minimum number of parenthesis that would need to be removed in order to make the string valid.
# "Valid" means that each open parenthesis has a matching closed parenthesis.
#
# Example:
#
# "()())()"
#
# The following input should return 1.
#
# ")("
#
# Here's a start:
# def count_invalid_parenthesis(string):
#   # Fill this in.
#
# print count_invalid_parenthesis("()())()")
# # 1

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return_value = self.stack[-1]
            self.stack = self.stack[:-1]
            return return_value
        else:
            print("stack is empty")

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True


def count_invalid_parenthesis(string):
    stack = Stack()
    count = 0
    for str in string:
        if str == "(":
            stack.push(str)
        elif str == ")":
            if stack.is_empty():
                count += 1
            else:
                stack.pop()
    return count


# Fill this in.

print(count_invalid_parenthesis("()())())()"))
# 1
