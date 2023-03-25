# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 루트가 비었을 경우 0
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        
        depth = 0

        # 큐가 빌 때까지 반복
        while queue:

            depth += 1  # 반복된 횟수 = 깊이

            # 큐에 들어 있는 노드들의 개수만큼 순회
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                # 왼쪽 노드가 존재한다면 큐에 삽입
                if cur_node.left:
                    queue.append(cur_node.left)
                # 오른쪽 노드가 존재한다면 큐에 삽입
                if cur_node.right:
                    queue.append(cur_node.right)

        # while문이 돌아간 만큼 = 노드 -> 자식노드.. 내려간 만큼
        return depth

