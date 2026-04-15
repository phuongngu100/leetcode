class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #DP easy
        res = []
        for n in range(numRows):
            row = [None for _ in range(n+1)] # initiate an array with space for that round, then fill top and bottom with 1 cause they always begin and start with 1
            row[0] = 1
            row[-1] = 1

            for j in range(1, len(row) -1):
                row[j] = res[n-1][j-1] + res[n-1][j] # n is the way down chieu doc, j is length chieu dai of an array 
            res.append(row)
        return res

        # time O(numRows^2) outer loop runs numRows times, for each iteration of outer loop, inner loop runs numRows times
        # spcae O(1)



        