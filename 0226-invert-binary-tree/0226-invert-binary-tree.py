# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 예외 처리
        if not root:
            return root
        
        
        def dfs(node: Optional[TreeNode]):
            
            # 종료 조건
            if not node:
                return
            
            
            # 양 쪽의 값을 교환
            node.left, node.right = node.right, node.left
            
            dfs(node.left)  # 왼쪽의 자식 노드로 재귀
            dfs(node.right) # 오른쪽의 자식 노드로 재귀
            
        dfs(root)
        
        
        return root