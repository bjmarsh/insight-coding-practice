"""
Given a list of integers S and a target number k, write a function that returns 
a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. 
You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, 
return [12, 9, 2, 1] since it sums up to 24.
"""

def get_subset(vals, target, istart=0):
    
    if istart >= len(vals):
        return None
    
    if istart == len(vals)-1:
        return [vals[-1]] if vals[-1] == target else None

    if vals[istart] == target:
        return [vals[istart]]

    if vals[istart] < target:
        subset = get_subset(vals, target-vals[istart], istart+1)
        if subset is not None:
            return [vals[istart]] + subset

    return get_subset(vals, target, istart+1)
    

if __name__ == "__main__":
    print(get_subset([],0))
    print(get_subset([12,1,61,5,9,2],24))
    print(get_subset([12],12))
    print(get_subset([12,1],12))
    print(get_subset([12,1,61,5,9,2],65))

