class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for l in range(len(temperatures)):
            r = l
            while r < len(temperatures) and temperatures[l] >= temperatures[r]:
                r += 1
            if r == len(temperatures):
                res.append(0)
            else:
                res.append(r - l)

        return res