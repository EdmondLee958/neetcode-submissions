class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        index = 0
        for i in nums:
            if (target - i) in hashmap:
                ans = hashmap[target - i]
                return [ans, index]
            hashmap[i] = index
            index += 1
        