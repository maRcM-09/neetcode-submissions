class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
            
        max_length = 1
        L = 0
        
        def isTurb(arr , L , R):
            isTurb1 = True # first turbulence case
            isTurb2 = True # second turbulence case
            for k in range(L,R):
                if k%2==0:
                    if (arr[k] >= arr[k+1]):
                        isTurb1 = False
                    if (arr[k] <= arr[k+1]):
                        isTurb2 = False
                else:
                    if arr[k] >= arr[k+1]:
                        isTurb2 = False
                    if arr[k] <= arr[k+1]:
                        isTurb1 = False
            return isTurb1 or isTurb2

        for R in range(1, len(arr)):
            if isTurb(arr, R-1, R):
                if not isTurb(arr, L, R):
                    L = R - 1
                max_length = max(max_length , R-L+1)
            else:
                L=R
        return max_length
