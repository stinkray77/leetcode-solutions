# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        NOT_COVERED = 0
        HAS_CAMERA = 1
        COVERED = 2

        cameras = 0

        def dfs(node):
            nonlocal cameras

            if not node:
                return COVERED
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == NOT_COVERED or right == NOT_COVERED:
                cameras += 1
                return HAS_CAMERA
            
            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED

            return NOT_COVERED
        
        if dfs(root) == NOT_COVERED:
            cameras += 1

        return cameras
