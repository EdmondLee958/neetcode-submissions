class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
    
    # bucket[i] = list of numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashmap.items():
            bucket[freq].append(num)
    
        res = []
        for freq in range(len(bucket) - 1, 0, -1):  # iterate high→low
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res








            


