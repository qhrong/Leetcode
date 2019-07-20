# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def traverse(Node):
            if Node:
                if Node.val <= R and Node.val >= L:
                    self.res += Node.val
                    # continue traverse node left and node right
                    traverse(Node.right)
                    traverse(Node.left)
                elif Node.val < L:
                    traverse(Node.right)
                elif Node.val > R:
                    traverse(Node.left)

        self.res = 0
        traverse(root)
        return self.res