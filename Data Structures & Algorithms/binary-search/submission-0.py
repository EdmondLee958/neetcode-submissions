class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        ans = -1

        for n in nums:
            if n == target:
                return index
            index += 1
        return ans
            