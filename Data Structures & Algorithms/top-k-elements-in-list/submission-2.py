class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        
        for i in range(k):
            ans.append(max(hashmap, key=lambda x: hashmap[x]))
            hashmap.pop(max(hashmap, key=lambda x: hashmap[x]))

        return ans



            


