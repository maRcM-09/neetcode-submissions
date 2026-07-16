class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        L = 0
        length = 1
        for R in range(1, len(s)):
            tmp = L
            nodup = True
            while tmp < R:
                if s[tmp] == s[R]:
                    L = tmp + 1
                    nodup = False
                    break
                tmp+=1
            length = max(length , R-L+1)
        return length