# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        max_depth, depth = 0, 1
        answer = []

        if root is None:
            return answer

        def dfs(node: Optional[TreeNode], depth):
            
            nonlocal max_depth

            # 종료 조건
            if not node:
                return
            
            if depth > max_depth:
                answer.append(node.val)
                max_depth = depth

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, depth)

        return answer
            

            


