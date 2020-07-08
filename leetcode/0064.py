class Solution(object):
    def minPathSum(self, grid, sr=0, sc=0, cache=None):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if cache is None:
            cache = [[-1]*len(grid[0]) for i in range(len(grid))]
        
        if sr==len(grid)-1 and sc==len(grid[0])-1:
            return grid[sr][sc]
        
        if cache[sr][sc] >= 0:
            return cache[sr][sc]
        
        paths = []
        if sr < len(grid)-1:
            paths.append(self.minPathSum(grid, sr+1, sc, cache=cache))
        if sc < len(grid[0])-1:
            paths.append(self.minPathSum(grid, sr, sc+1, cache=cache))
    
        
        minpath = grid[sr][sc] + min(paths)
        cache[sr][sc] = minpath
        
        return minpath
