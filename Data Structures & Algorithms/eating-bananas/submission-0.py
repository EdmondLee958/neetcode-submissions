class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            curr_h = 0

            for i in piles:
                curr_h += math.ceil(float(i) / k)
            if curr_h <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

