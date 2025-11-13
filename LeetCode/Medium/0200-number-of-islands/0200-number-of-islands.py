class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        def dfs(i, j):
            # 종료조건 : 땅이 아니면
            if i < 0 or j >=len(grid[0]) or j < 0 or i >= len(grid) or grid[i][j]!='1': return
            # 초기화
            grid[i][j] = 0
            #그래프 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt +=1
        
        return cnt
            
                
        