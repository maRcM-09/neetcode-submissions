# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_node(self,root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right , key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_Node = self.min_node(root.right)
                root.val = min_Node.val
                root.right = self.deleteNode(root.right, min_Node.val)
        return root

        

        