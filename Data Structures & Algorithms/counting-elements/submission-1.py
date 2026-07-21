class Solution:
    def countElements(self, arr: List[int]) -> int:
        n_elem = 0
        for number in arr:
            if number + 1 in arr:
                n_elem+=1
        return n_elem
            
        