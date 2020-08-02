"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def solution(vals):

    best_p1 = vals[0]
    best_p2 = 0
    for x in vals[1:]:
        best = max([x, x + best_p2, best_p1])
        best_p2 = best_p1
        best_p1 = best
    return best

if __name__ == "__main__":
    print(solution([2, 4, 6, 2, 5])) # 13
    print(solution([5, 1, 1, 5])) # 10
    print(solution([0,0,0,0])) # 0
    print(solution([-1,-2,-3,-4])) #-1
    print(solution([-9,-8,-7,-1,-4,-5])) #-1




