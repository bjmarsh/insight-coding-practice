class Solution:
    def twoSumClosest(self, nums, target, startidx=0):
        """ assume nums is sorted """
        
        i, j = startidx, len(nums)-1
        bestdiff, bestsum = None, None
        while i < j:
            tot = nums[i] + nums[j]
            if tot==target:
                return target
            if bestdiff is None or abs(tot-target) < bestdiff:
                bestsum = tot
                bestdiff = abs(tot - target)

            if tot < target:
                i += 1
            else:
                j -= 1
        
        return bestsum
        
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        snums = sorted(nums)
        best = 0
        ans = None
        for istart in range(0, len(snums)-2):
            closest = snums[istart] + self.twoSumClosest(snums, target-snums[istart], istart+1)
            if ans is None or abs(closest-target) < best:
                ans = closest
                best = abs(closest-target)
        
        return ans
