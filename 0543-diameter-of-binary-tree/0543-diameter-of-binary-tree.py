# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # 가장 긴 경로의 길이
        longest_length = 0

        def dfs(node: Optional[TreeNode]) -> int:
            # 노드가 비었을 경우 -1의 값을 반환한다.
            if not node:
                return - 1
            
            # 왼쪽, 오른쪽 각각의 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로의 길이
            nonlocal longest_length
            longest_length = max(longest_length, left + right + 2)
            
            # 상태값
            return max(left, right) + 1
        
        dfs(root)

        return longest_length