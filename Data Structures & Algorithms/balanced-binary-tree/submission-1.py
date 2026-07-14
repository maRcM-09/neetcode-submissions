class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def compute_height(root):
            if not root:
                return 0
            left_h = 1 + compute_height(root.left)
            right_h = 1 + compute_height(root.right)
            return max(left_h , right_h)
        
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
            
        height_left = compute_height(root.left)
        height_right = compute_height(root.right)
        return abs(height_left - height_right) <= 1