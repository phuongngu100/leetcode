class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) -1
        while l <= r:
            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1

        return l
        