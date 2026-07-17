class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = set(s)
        max_length = 0
        for char in characters:
            L = 0
            changes = 0
            for R in range(len(s)):
                if s[R] != char:
                    changes+=1
                while changes > k:
                    if s[L] != char:
                        changes -= 1
                    L+=1
                max_length = max(max_length , R-L+1)
        return max_length
