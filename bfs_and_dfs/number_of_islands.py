class Solution(object):
    def dfs(self, grid, r, c): 
        nr = len(grid)
        nc = len(grid[0])
        if grid[r][c] == "0":
            return
        grid[r][c] = "0";
       
        if (r - 1 >= 0) and (grid[r-1][c] == "1"):
            self.dfs(grid, r-1, c)
        if (r + 1 < nr) and (grid[r+1][c] == "1"):
            self.dfs(grid, r+1, c)
        if (c - 1 >= 0) and (grid[r][c-1] == "1"):
            self.dfs(grid, r, c-1)
        if (c + 1 < nc) and (grid[r][c+1] == "1"):
            self.dfs(grid, r, c+1)
        
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if nr == 0: 
            return 0
        
        nc = len(grid[0])
        
        num_island = 0
        
        for r in range(0, nr):
            for c in range(0, nc):
                if grid[r][c] == '1':
                    num_island += 1
                    self.dfs(grid, r, c)

        
        return num_island