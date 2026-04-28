class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        ans = []
        index = 0
        for i in nums:
            if target - i in hashmap:
                ans.append(hashmap.get(target - i))
                ans.append(index)
                return ans
            hashmap[i] = index
            index += 1
