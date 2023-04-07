class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):    # i: 행, j: 열
            # 종료 조건 (범위를 벗어나거나 육지가 아닌 경우)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            
            # 방문 처리. 현재 육지(1)를 물(0)로 바꿔서 다시 방문하지 못하도록 한다.
            grid[i][j] = "0"

            # 상하좌우 재귀
            dfs(grid, i-1, j)   # 상
            dfs(grid, i+1, j)   # 하
            dfs(grid, i, j-1)   # 좌
            dfs(grid, i, j+1)   # 우

        # 예외 처리
        if not grid:
            return 0
        
        cnt = 0 # 방문 횟수
        
        # 이중 반복문을 통해 모든 칸을 확인한다.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 육지(1)일 경우 방문
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    cnt += 1    # 방문 횟수 + 1

        return cnt
