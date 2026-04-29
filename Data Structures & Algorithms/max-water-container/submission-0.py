class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        possible = []
        while i < j:
            x = j - i
            water = x * min(heights[i],heights[j])
            possible.append(water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max(possible)