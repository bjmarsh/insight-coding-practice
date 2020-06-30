class Solution(object):
    def floodFill(self, image, sr, sc, newColor, oldColor=None):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        # [[1,1,1],
        #  [1,1,0],
        #  [1,0,1]]
        
        if oldColor is None:
            oldColor = image[sr][sc]
            
        if image[sr][sc] == newColor:
            return image
        
        image[sr][sc] = newColor
        
        if sr > 0 and image[sr-1][sc] == oldColor:
            self.floodFill(image, sr-1, sc, newColor, oldColor)
        
        if sr < len(image)-1 and image[sr+1][sc] == oldColor:
            self.floodFill(image, sr+1, sc, newColor, oldColor)
        
        if sc > 0 and image[sr][sc-1] == oldColor:
            self.floodFill(image, sr, sc-1, newColor, oldColor)
        
        if sc < len(image[0])-1 and image[sr][sc+1] == oldColor:
            self.floodFill(image, sr, sc+1, newColor, oldColor)
            
        return image
        
