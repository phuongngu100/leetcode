class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows
        if numRows == 1:
            return s
        cur = 0
        direction = 1
        
        for c in s:
            res[cur] += c
            if cur == 0:
                direction = 1
            # move up after reach final row
            elif cur == numRows - 1:
                direction = -1
            cur += direction
        return ''.join(res)




