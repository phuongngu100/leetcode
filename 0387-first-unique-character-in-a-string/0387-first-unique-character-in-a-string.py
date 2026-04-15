class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = Counter(s)

        for i, c in enumerate(s): #loop through the string, get char position i and char c
            if repeat[c] == 1:
                return i
        return -1
        
        