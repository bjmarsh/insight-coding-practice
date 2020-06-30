class Solution(object):
    def minPathSum(self, grid, sr=0, sc=0, cache={}):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if sr==0 and sc==0:
            # why is this necessary? Submission seems to be doing
            # something fishy with this variable, "remembering" it
            # between different test cases
            cache = {}
        
        if sr==len(grid)-1 and sc==len(grid[0])-1:
            return grid[sr][sc]
        
        if (sr,sc) in cache:
            return cache[(sr,sc)]
        
        paths = []
        if sr < len(grid)-1:
            paths.append(self.minPathSum(grid, sr+1, sc, cache=cache))
        if sc < len(grid[0])-1:
            paths.append(self.minPathSum(grid, sr, sc+1, cache=cache))
    
        
        minpath = grid[sr][sc] + min(paths)
        cache[(sr,sc)] = minpath
        print(sr,sc,minpath)
        return minpath

