"""
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and 
you do not need to store the results. You can simply print them out as you compute them.
"""

def solution(vals, k):
    
    ans = []
    
    # # Brute-force
    # # O((n-k+1)*k) time
    # # O(1) space
    # for istart in range(0, len(vals)-k+1):
    #     ans.append(max(vals[istart:istart+k]))
        
    # use a double-ended queue
    # deq will store elements in current window, that are larger than all
    # elements to the right of it in the window
    # O(n) time
    # O(k) space
    deq = deque()
    
    # process first window
    for i in range(k):
        while len(deq) > 0 and vals[deq[-1]] < vals[i]:
            deq.pop()
        deq.append(i)
        
    # loop through rest of array
    for i in range(k, len(vals)):
        ans.append(vals[deq[0]])
        if deq[0] < i-k+1:
            deq.popleft()
        while len(deq) > 0 and vals[deq[-1]] < vals[i]:
            deq.pop()
        deq.append(i)
    
    # add element from last window
    ans.append(vals[deq[0]])
    
    return ans

    
if __name__ == "__main__":
    print(solution([10,5,2,7,8,7))
