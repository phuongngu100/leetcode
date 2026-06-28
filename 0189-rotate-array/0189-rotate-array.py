class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # start = starting position of the cycle
        # count = how many elements we have moved
        count = start = 0

        while count < n: # the loop stop when we have moved all the elements around
            cur, prev = start, nums[start]
            while True:
                next_idx = (cur + k) % n 
                nums[next_idx], prev = prev, nums[next_idx] #switch
                # after this line the array becomes 1,2,3,1,5,6,7
                # 4 is stored in variable prev
                cur = next_idx
                count +=1
                if start == cur:
                    break
            start +=1

        # O(n) time
        # O(1) space
            

        
        