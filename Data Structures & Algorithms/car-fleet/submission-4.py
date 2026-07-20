class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pv_map = {p:v for p,v in zip(position, speed)}
        def k(car):
            return (target - car[0])/car[1]
        n_fleets = 0
        position.sort(reverse=True)
        stack=[]
        for p in position:
            new_car = (p,pv_map[p])
            k_new = k(new_car)
            if not stack or k_new > stack[-1]:
                stack.append(k_new)
                n_fleets+=1
        return n_fleets
            