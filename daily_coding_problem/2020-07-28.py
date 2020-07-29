"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
"""

def solution(nums):
    
    # first, replace all zeros and negative numbers by len(nums)+2
    # (this will not affect answer, as it must be in [1,len(nums)+1]
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i] = len(nums)+2
    
    # Now consider all numbers in [1,len(nums)] missing
    # if we find a number x in this range, make the number at index x-1 negative
    for x in nums:
        if 1 <= abs(x) <= len(nums):
            nums[abs(x)-1] = -abs(nums[abs(x)-1])

    # now get the index of the first postive number
    for i,x in enumerate(nums):
        if x > 0:
            return i+1
    # if all are negative, then we've covered everytihng in [1,len(nums)], so answer is len(nums)+1
    return len(nums)+1
        

if __name__ == "__main__":
    print(solution([3,4,-1,1,1,1,0]))
    print(solution([1,2,0]))
    print(solution([1,2,3]))
    print(solution([]))

