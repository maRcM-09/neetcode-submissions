# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_value = preorder[0]
        root_index = inorder.index(root_value)

        root = TreeNode(root_value)
        
        left_subtree_inorder = inorder[:root_index]
        right_subtree_inorder = inorder[root_index+1:]
        
        left_subtree_preorder = preorder[1:1 + len(left_subtree_inorder)]
        right_subtree_preorder = preorder[1 + len(left_subtree_inorder):]

        root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)
        return root
