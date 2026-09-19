# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        # prefix sum
        prefix_count = {0:1}

        def dfs(root, curSum):
            if not root:
                return 0
            curSum += root.val
            count = prefix_count.get(curSum - targetSum, 0) 
            prefix_count[curSum] = prefix_count.get(curSum, 0) + 1

            count += dfs(root.left, curSum)
            count += dfs(root.right, curSum)

            prefix_count[curSum] -= 1
            return count
        return dfs(root, 0)


        