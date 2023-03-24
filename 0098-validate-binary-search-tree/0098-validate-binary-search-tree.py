# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder: list = []

        def dfs(node: Optional[TreeNode]):
            
            if node is None:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        
        for i in range(len(inorder)):
            if i+1 < len(inorder) and inorder[i] >= inorder[i+1]:
                return False
            
        return True