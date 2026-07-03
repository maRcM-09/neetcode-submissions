class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        for i in range(len(arr)-1):
            maxi = arr[i+1]
            for j in range(i+1,len(arr)):
                maxi = max(arr[j] , maxi)
            arr[i] = maxi
        arr[n] = -1
        return arr

        