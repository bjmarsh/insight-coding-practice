class Solution:
    def rob(self, nums: List[int], istart=0, cache=None) -> int:
        
        if cache is None:
            cache = {}
        
        if istart in cache:
            return cache[istart]
        
        if istart >= len(nums):
            return 0
        
        if len(nums) - istart <= 2:
            return max(nums[istart:])
        
        option1 = nums[istart] + self.rob(nums, istart+2, cache=cache)
        option2 = nums[istart+1] + self.rob(nums, istart+3, cache=cache)
        
        cache[istart] = max(option1, option2)
        
        return cache[istart]
