class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        a = len(grid)
        b = len(grid[0])
        
        cnt = 0
        visited = [[False] * b for _ in range(a)]
        queue = deque()

        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(a):
            for j in range(b):

                # 땅이 아니라면 무시
                if grid[i][j] == "0":
                    continue

                # 방문했다면 무시
                if visited[i][j] == True:
                    continue
                
                queue.append((i, j))
                visited[i][j] = True
                cnt += 1

                while queue:

                    x, y = queue.popleft()

                    # 상하좌우
                    for k in range(0, 4):
                        
                        # 현재 위치에서의 상하좌우
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # 만약 map을 벗어날 경우 무시
                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                            continue

                        # 만약 방문했을 경우 무시
                        if visited[nx][ny] == True:
                            continue

                        # 만약 상하좌우가 0인 경우 무시
                        if grid[nx][ny] == "0":
                            continue

                        visited[nx][ny] = True
                        queue.append((nx, ny))

        return cnt