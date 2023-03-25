# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:       
        # 루트가 없을 경우 True
        if root is None:
            return True

        def dfs(leftNode: Optional[TreeNode], rightNode:Optional[TreeNode]):
            # left와 right가 모두 없을 경우 True
            if leftNode is None and rightNode is None:
                return True
            
            # left 혹은 right 둘 중 하나가 없을 경우 False
            if leftNode is None or rightNode is None:
                return False
            
            # left와 right가 다를 경우 False
            if leftNode.val != rightNode.val:
                return False
            
            # 왼쪽 노드의 왼쪽 값과 오른쪽 값
            left_right = dfs(leftNode.left, rightNode.right)

            # 오른쪽 노드의 오른쪽 값과 왼쪽 값
            right_left = dfs(leftNode.right, rightNode.left)

            return left_right and right_left
        
        return dfs(root.left, root.right)