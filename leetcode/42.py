class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        high = -1
        units = [0] * len(height)
        for i,h in enumerate(height):
            print i, h
            if h < high:
                units[i] = high-h
            else:
                high = h
                
                
        high = -1
        for i,h in enumerate(height[::-1]):
            print i, h
            if h < high:
                units[-i-1] = min(high-h, units[-i-1])
            else:
                units[-i-1] = 0
                high = h
        
        print(units)
        return sum(units)
