class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numHash = Counter(nums)
        numHash = defaultdict(int)
        for i in nums:
            numHash[i] +=1
        
        for i in numHash:
            if numHash[i] == 1:
                return i
        # time O(n) time since loop through is O(n) and space is also O(n) for the hash table
        