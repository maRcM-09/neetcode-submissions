class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        element_index = 0
        res = None
        def dfs(node):
            nonlocal element_index, res
            if not node or res is not None:
                return 
            dfs(node.left)
            element_index += 1
            if element_index == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res