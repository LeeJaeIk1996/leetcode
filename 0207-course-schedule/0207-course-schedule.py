class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 그래프 만들기
        graph = [[] for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        
        # 각 노드의 방문 여부 저장
        visited = [0 for _ in range(numCourses)]
        
        def dfs(node):
            # 이미 방문한 노드를 다시 방문하면 순환 구조가 있다는 의미
            if visited[node] == -1:
                return False
            # 이미 방문한 노드인 경우
            if visited[node] == 1:
                return True
            
            # 방문 표시
            visited[node] = -1
            
            # 이어진 노드들에 대해 DFS 수행
            for i in graph[node]:
                if not dfs(i):
                    return False
            
            # 방문 완료 표시
            visited[node] = 1
            return True
        
        # 모든 노드에 대해 DFS 수행
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
