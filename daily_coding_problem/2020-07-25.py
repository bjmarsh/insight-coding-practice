from typing import List

def solution(nums: List[int], k: int) -> bool:
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    """
    
    # # brute-force, O(n^2) time, O(1) space
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == k:
    #             return True
    # return False

    # # O(n) time, O(n) space
    # seen = set()
    # for x in nums:
    #     if k - x in seen:
    #         return True
    #     seen.add(x)
    # return False

    # O(n log n) time, O(1) space
    nums.sort()
    i = 0
    j = len(nums) - 1
    while j > i:
        val = nums[i] + nums[j]
        if val == k:
            return True
        elif val < k:
            i += 1
        else:
            j -= 1
    return False

if __name__ == "__main__":
    print(solution([10, 15, 3, 7], 17))
    print(solution([10, 15, 3, 7], 19))
    print(solution([10, 15, 3, 7], 30))
