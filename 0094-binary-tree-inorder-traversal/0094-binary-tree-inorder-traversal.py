# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(root: Optional[TreeNode]):
            # 종료 조건
            if root is None:
                return
            
            dfs(root.left)
            answer.append(root.val)
            dfs(root.right)

        dfs(root)
        return answer