class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hash = {}
        for i in range(len(position)):
            hash[position[i]] = speed[i]

        position.sort()
        fleets = []
        for p in position[::-1]:
            fleets.append((target - p) / hash[p])

            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
                
        return len(fleets)