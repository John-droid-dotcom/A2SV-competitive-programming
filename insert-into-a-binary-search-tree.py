# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        dummy = root
        def insert(root, val):
            if root.val > val:
                if not root.left:
                    node = TreeNode(val)
                    root.left = node
                    return 
                return insert(root.left, val)
            else:
                if not root.right:
                    node = TreeNode(val)
                    root.right = node
                    return 
                return insert(root.right, val)

        insert(root, val)
        return dummy