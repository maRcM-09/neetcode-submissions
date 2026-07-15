class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        running_sum = 0
        L = 0
        for R in range(len(arr)):
            running_sum += arr[R]
            if R-L >= k-1:
                if (running_sum/k) >= threshold:
                    ans+=1
                running_sum -= arr[L]
                L+=1
        return ans