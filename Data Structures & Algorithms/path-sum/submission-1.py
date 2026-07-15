# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def explore_sum(root, s):
            s += root.val
            if not root.left and not root.right:
                return s==targetSum
            sl = explore_sum(root.left,s) if root.left else False
            sr = explore_sum(root.right, s) if root.right else False
            return sl or sr
        return explore_sum(root,0)