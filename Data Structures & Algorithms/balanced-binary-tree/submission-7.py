class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            h_left = 1 + height(root.left)
            h_right = 1 + height(root.right)
            return max(h_left , h_right)
        def balanced(root):
            if not root:
                return True
            h_left_subtree = height(root.left)
            h_right_subtree = height(root.right)
            if abs(h_left_subtree - h_right_subtree) > 1:
                return False
            return balanced(root.left) and balanced(root.right)

        return balanced(root)