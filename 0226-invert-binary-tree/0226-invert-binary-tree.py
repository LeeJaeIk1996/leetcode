# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode]):
            # 종료 조건. 즉, 더이상 node가 없을 경우 return한다.
            if not node:
                return

            # 왼쪽과 오른쪽 각각을 탐색
            dfs(node.left)
            dfs(node.right)

            # 현재의 노드에서 노드의 왼쪽과 오른쪽을 바꿔준다.
            node.left, node.right = node.right, node.left

        dfs(root)

        return root