# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        bst = []
        answer = 0

        def dfs(node:Optional[TreeNode]):
            # 종료 조건
            if not node:
                return
            
            dfs(node.left)
            bst.append(node.val)
            dfs(node.right)

        dfs(root)
        
        for i in range(len(bst)):
            if i == k-1:
                answer = bst[i]

        return answer