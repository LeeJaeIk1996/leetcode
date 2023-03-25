# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 루트가 비었을 경우 0
        if root is None:
            return 0
        
        max_depth = 1
        depth = []   # 깊이를 저장하는 배열
        
        def dfs(node: Optional[TreeNode], max_depth):

            # 왼쪽 노드가 존재할 경우
            if node.left:
               dfs(node.left, max_depth + 1)

            # 오른쪽 노드가 존재할 경우
            if node.right:
                dfs(node.right, max_depth + 1)

            depth.append(max_depth)

        dfs(root, max_depth)

        return max(depth)