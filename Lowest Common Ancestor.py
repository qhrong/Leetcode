# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Recursive method

        # value of parent node
        parent_val = root.val
        # value of p
        p_val = p.val
        # value of q
        q_val = q.val

        # if both p and q are on the right
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if both p and q are on the left
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

            # Iterative method
        # value of parent node
        parent_val = root.val
        # value of p
        p_val = p.val
        # value of q
        q_val = q.val

        while node:
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
