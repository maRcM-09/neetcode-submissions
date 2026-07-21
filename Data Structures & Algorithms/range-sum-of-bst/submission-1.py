# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        self.sum = 0
        def isInRange(root):
            if not root:
                return 0
            if root.val <= high and root.val >= low:
                self.sum += root.val
            isInRange(root.left)
            isInRange(root.right)
        isInRange(root)
        return self.sum
