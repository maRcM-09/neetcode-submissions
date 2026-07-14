# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # leaf case
        if not preorder or not inorder:
            return None
        # build root node
        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)
        
        # find left and right subtrees inorder
        left_subtree_inorder = inorder[:root_idx]
        right_subtree_inorder = inorder[root_idx+1:]

        # find left and right subtrees preorder
        left_subtree_preorder = preorder[1:1+len(left_subtree_inorder)]
        right_subtree_preorder = preorder[1+len(left_subtree_inorder):]

        # recursive calls to build left and right subtrees
        root.left = self.buildTree(left_subtree_preorder ,left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder ,right_subtree_inorder)

        return root