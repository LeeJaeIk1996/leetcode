# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal max_path
            # 종료 조건
            if not node:
                return
            
            left_max = dfs(node.left) or 0
            right_max = dfs(node.right) or 0

            # 현재 노드를 포함하는 경로의 최대값
            max_path_sum = node.val + max(left_max, 0) + max(right_max, 0)

            # 전체 트리에서 최대 경로 합을 갱신
            max_path = max(max_path, max_path_sum)

            # 현재 노드를 루트로 하는 서브트리에서의 최대 경로 합
            return node.val + max(left_max, right_max, 0)
        
        dfs(root)

        return max_path