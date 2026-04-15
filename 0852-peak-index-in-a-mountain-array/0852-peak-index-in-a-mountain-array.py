class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) -1

        while l <r:
            mid = (l+r) // 2
            if arr[mid] < arr[mid+1]: # peak is greater than mid
                l = mid+1
            else: #peak is either mid or some index smaller than mid
                r = mid
        return l





        # time worst case O(n) cause still have to traverse the whole thing
        # while l <= r:
        #     if arr[l] < arr[r]:
        #         l += 1
        #     else:
        #         r -= 1

        # return l
        