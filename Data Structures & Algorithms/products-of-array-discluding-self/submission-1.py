class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in range(len(nums)):
            total = 1
            for i in range(len(nums)):
                if i != n:
                    total = total * nums[i]
            res.append(total)

        return res