class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        cur = self.root
        while cur:
            parent = cur
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                cur.val = val
                return
        if key > parent.key:
            parent.right = TreeNode(key, val)
        else:
            parent.left = TreeNode(key, val)

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val 

    def recursive_removal(self, key, root):
        if not root:
            return None
        if key > root.key:
            root.right = self.recursive_removal(key, root.right)
        elif key < root.key:
            root.left = self.recursive_removal(key, root.left)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.key, root.val = cur.key, cur.val
                root.right = self.recursive_removal(cur.key, root.right)
        return root

    def remove(self, key: int) -> None:
        self.root = self.recursive_removal(key, self.root)

    def getInorderKeys(self) -> List[int]:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.key)
                inorder(node.right)
        inorder(self.root)
        return res