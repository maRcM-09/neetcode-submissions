class Solution:

    def origin_distance(self,point):
        x,y=point[0],point[1]
        if x == 0:
            return abs(y)
        elif y==0:
            return abs(x)
        else:
            return math.sqrt(x**2 + y**2)
    def merge(self,arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        i = 0
        j=0
        k=s
        while i < len(L) and j < len(R):
            if self.origin_distance(L[i]) <= self.origin_distance(R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            arr[k] = R[j]
            k+=1
            j+=1
        
    def merge_sort(self, arr , s, e):
        if e-s+1<=1:
            return arr
        m=(s+e)//2
        self.merge_sort(arr,s,m)
        self.merge_sort(arr,m+1,e)
        self.merge(arr,s,m,e)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 1:
            return points
        self.merge_sort(points, 0, len(points) - 1)
        return points[:k]