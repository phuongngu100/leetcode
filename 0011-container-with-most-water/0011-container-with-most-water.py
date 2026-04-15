class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        res = 0

        while i < j:
            res = max(res, min(height[i],height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1 # cause if move j down its gonna spill anyway caus i smaller
            else:
                j -= 1
        return res

        