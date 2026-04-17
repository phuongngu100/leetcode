class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numHash = Counter(nums)
        
        for i,c in enumerate(nums):
            if numHash[c] == 1:
                return nums[i]
        