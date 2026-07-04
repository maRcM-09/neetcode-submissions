class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'(': 1,'[': 2,'{': 3,
        '}': 4,']': 5,')': 6}
        stack = []
        if len(s) < 2:
            return False
        for char in s:
            if chars[char] <= 3: 
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                open_char = stack.pop()
                if chars[open_char] + chars[char] != 7:
                    return False
        return len(stack)==0


