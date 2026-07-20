class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pv_map = { p : v for p,v in zip(position, speed)}
        # sort the positions
        position.sort(reverse=True)
        def reach_target(car):
            p , v = car
            return (target - p) / v
        n_fleets = 0
        stack = []
        for p in position:
            new_car = (p , pv_map[p])
            if not stack or reach_target(new_car) > stack[-1]:
                stack.append(reach_target(new_car))
                n_fleets += 1
        return n_fleets