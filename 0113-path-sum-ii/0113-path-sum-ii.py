# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []

        def backtrack(root, target, path):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right:
                if target == 0:
                    res.append(path.copy())
            backtrack(root.left,target,path)
            backtrack(root.right,target,path)

            path.pop()
        backtrack(root, targetSum, [])
        return res

            
            