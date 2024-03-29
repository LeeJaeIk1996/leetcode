# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root:
            if root == p or root == q:
                return root
            
            leftnode = self.lowestCommonAncestor(root.left, p, q)
            rightnode = self.lowestCommonAncestor(root.right, p, q)
            
            if leftnode and rightnode:
                return root
            elif rightnode:
                return rightnode
            else:
                return leftnode