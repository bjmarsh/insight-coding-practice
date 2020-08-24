"""
You are given an array of non-negative integers that represents a two-dimensional elevation map 
where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, 
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
so we can trap 8 units of water.
"""

def solution(heights):

    # # O(n) time and O(n) space
    # curmax = 0
    # water = [0] * len(heights)
    # for i in range(len(heights)):
    #     if heights[i] < curmax:
    #         water[i] = curmax - heights[i]
    #     curmax = max(curmax, heights[i])

    # curmax = 0
    # for i in range(len(heights)-1,-1,-1):
    #     tmp = 0
    #     if heights[i] < curmax:
    #         tmp = curmax - heights[i]
    #     water[i] = min(water[i], tmp)
    #     curmax = max(curmax, heights[i])

    # return sum(water)


    # O(n) time, O(1) space
    ileft, iright = 0, len(heights) - 1
    leftmax, rightmax = 0, 0
    ans = 0
    while ileft < iright:
        if heights[ileft] < heights[iright]:
            if heights[ileft] >= leftmax:
                leftmax = heights[ileft]
            else:
                ans += leftmax - heights[ileft]
            ileft += 1
        else:
            if heights[iright] >= rightmax:
                rightmax = heights[iright]
            else:
                ans += rightmax - heights[iright]
            iright -= 1
    return ans


if __name__ == "__main__":
    print(solution([3,0,1,3,0,5]))
    print(solution([3,2,1,0]))


#      x 
#      x
# x  x x
# x  x x
# x xx x
# ---------------
