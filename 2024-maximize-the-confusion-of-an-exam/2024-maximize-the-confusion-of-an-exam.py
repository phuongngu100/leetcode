class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        res = 0
        count = { 'T': 0, 'F': 0}

        l = 0 
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1 # whatever it is plus 1
            # check if the length of the window - max number of whatever it is max, if it's bigger than k means we cant change anymore and move the window

            if (r-l+1) - max(count['T'], count['F']) > k:
                count[answerKey[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


        