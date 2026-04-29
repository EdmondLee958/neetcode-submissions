class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        index = 1
        for i in numbers:
            temp_index = 1
            for j in numbers:
                if i != j and i + j == target:
                    res.append(index)
                    res.append(temp_index)
                    return res
                temp_index += 1
            index += 1
        
        return res
        

