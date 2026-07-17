class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        length = 1
        L = 0
        R = 1
        
        while R < n:
            tmp = L
            no_dup = True
            while tmp < R:
                if s[tmp] == s[R]:
                    L = tmp + 1
                    nodup = False
                    break
                tmp+=1
            length = max(length , R-L+1)
            R+=1
        return length
            