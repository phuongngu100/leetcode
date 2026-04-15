class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        longest = 0
        # initalize the first index
        start = 0

        for c in range(len(s)):
            while s[c] in stringSet:
                stringSet.remove(s[start])
                start += 1
            stringSet.add(s[c])
            longest = max(longest, c - start + 1)
        return longest
        # O(n) since you have only to loop through the string once
        

        

        