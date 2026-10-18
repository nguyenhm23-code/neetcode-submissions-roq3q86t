class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) 
        visit = set()
        res = 0
        r, c = 0, 0
        def dfs(r, c):
            if c < 0 or r < 0 or c > cols - 1 or r > rows - 1 or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c)) 
            return (1 + dfs(r,c+1) + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1)) 
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j)) 
        return res