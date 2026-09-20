# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []

        def backtrack(path, root):
            if not root:
                return []
            path +=str(root.val)
            if not root.right and not root.left:
                res.append(path)
            path += '->'
            backtrack(path, root.left)
            backtrack(path, root.right)
            # path.pop()
        backtrack('', root)
        return res


        
        