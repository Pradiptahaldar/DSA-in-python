class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != char:
                    return False
        return len(stack) == 0
#another approach
class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return not stack