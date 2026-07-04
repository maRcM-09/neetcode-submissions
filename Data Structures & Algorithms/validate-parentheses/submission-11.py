class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')': '(',']': '[','}': '{'}
        stack = []
        for char in s:
            if char in chars: # is an open bracket 
                if stack and stack[-1] == chars[char]:
                    stack.pop()
                else:
                    return False
            else: # is a closed parenthesis
                stack.append(char)
        return True if not stack else False


