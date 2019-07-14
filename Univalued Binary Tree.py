# Definition for a binary tree node.
# class TreeNode:
#      def __init__(self, x):
#          self.val = x
#          self.left = None
#          self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        if not root:
            return True

        if root:
            if root.left:
                if root.val != root.left.val:
                    return False
            if root.right:
                if root.val != root.right.val:
                    return False
            return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
