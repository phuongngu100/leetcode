class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we will use a stack to keep track of the open parenthesis
        stack = []
        res = []

        def backtrack(openN, closeN):
            # base case:
            if openN == closeN == n:
                res.append("".join(stack)) # return all that in the stack
                return res
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res
            






        # stack = []
        # res = []

        # # for example, n=2
        # # ()() and (()) are all the valid answers
        # # backtrack happens when
        # def backtracking(openN, closedN):
        #     # used all the parenthesis
        #     if openN == closedN == n:
        #         # join the elements in the stack together
        #         res.append("".join(stack))
        #         return res
        #     if openN < n: # when open < n meaning we can still add more open
        #         stack.append("(")
        #         backtracking(openN + 1, closedN)
        #         stack.pop() # remove and try other options
        #     # we can only add ) if there are more ( used (to stay valid)
        #     if closedN < openN:
        #         stack.append(")")
        #         backtracking(openN, closedN + 1)
        #         stack.pop()
        # backtracking(0,0)
        # return res
        