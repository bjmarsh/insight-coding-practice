from typing import List

def solution(nums: List[int]) -> List[int]:
    """
    Given an array of integers, return a new array such that each element at index i 
    of the new array is the product of all the numbers in the original array 
    except the one at i
    """
 
    # # O(n) time (2 passes through list), O(1) space (not counting return list)
    # prod = 1
    # prod_nonzero = 1
    # num_zero = 0
    # for x in nums:
    #     prod *= x
    #     if x == 0:
    #         num_zero += 1
    #     else:
    #         prod_nonzero *= x

    # if num_zero > 1:
    #     return [0]*len(nums)

    # ret = []
    # for x in nums:
    #     if x==0:
    #         ret.append(prod_nonzero)
    #     else:
    #         ret.append(prod // x)
    # return ret

    # Now not using division. O(n^2) time, O(1) space
    ret = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            prod *= nums[j]
            if prod == 0:
                break
        ret.append(prod)
    return ret

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([3, 2, 1]))
    print(solution([1,2,3,0,4]))
    print(solution([1,2,3,0,4,0]))
