class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # O(n^2) time, O(1) space
        
        besthigh = 0
        bestarea = 0
        for ileft in range(len(height)-1):
            if height[ileft] == 0:
                continue
            if height[ileft] <= besthigh:
                continue
            besthigh = max(besthigh, height[ileft])
            minwidth = int(bestarea / height[ileft]) + 1
            for iright in range(ileft+minwidth, len(height)):
                area = (iright-ileft) * min(height[ileft], height[iright])
                bestarea = max(area, bestarea)
                
        return bestarea
