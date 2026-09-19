class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtrack(perm)
                    perm.pop()
        backtrack([])
        return res





















#         if len(nums) == 0:
#             return [[]]
#         # it computes the permutations for the rest of the list (excluding the first element)
#         perms = self.permute(nums[1:]) # reducing the problem size step by step since all the permutations can be a sub problem of a larger problem
#         '''
# Base Case: When the list has only one element, the permutation is trivially the list itself. This is the simplest case and provides a stopping point for recursion.
# Recursive Step: For a list with more than one element, the problem is divided into smaller subproblems: generate permutations of the sublist (excluding the first element) and then insert the excluded element in all possible positions of these permutations.
# '''
#         res = []
#         # reinsert nums[0] (the first element of the original list) into every possible position in each of the permutations (p) of nums[1:]
#         for p in perms:
#             # For each permutation p in perms, the function creates a copy of p (p_copy), and then inserts nums[0] at every possible index i (from 0 to len(p))
#             for i in range(len(p) + 1):
#                 p_copy = p.copy()
#                 p_copy.insert(i, nums[0])
#                 res.append(p_copy)
#         return res

#         # The time complexity of this algorithm is O(n * n!):
# # There are n! permutations of n elements.
# # For each permutation, you are inserting the removed element into n possible positions (so you do work proportional to n for each permutation).

# # Space Complexity:
# # The space complexity is O(n * n!) as well, due to the storage required for all the permutations and recursive calls.


        