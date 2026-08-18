class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)

        for i in range (0, k - 1):
            heapq.heappop(nums)

        res = heapq.heappop(nums) * -1
        return res