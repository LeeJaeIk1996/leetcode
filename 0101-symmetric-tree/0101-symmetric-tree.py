# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 루트가 없을 경우 True
        if root is None:
            return True

        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()

            # 왼쪽과 오른쪽 모두 비었을 경우 
            if leftNode is None and rightNode is None:
                continue
            
            # 왼쪽 혹은 오른쪽 하나만 비었을 경우 
            if leftNode is None or rightNode is None:
                return False
            
            # 왼쪽 값과 오른쪽 값이 다른 경우
            if leftNode.val != rightNode.val:
                return False
            
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            
            queue.append(leftNode.right)
            queue.append(rightNode.left)

        # 아무 이상 없을 경우 True를 반환
        return True

