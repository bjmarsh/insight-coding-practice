"""
A builder is looking to build a row of N houses that can be of K different colors. 
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the 
nth house with kth color, return the minimum cost which achieves this goal.
"""

def solution(costs, start_n=0, disallowed_color=None, cache=None):
    """
    costs is an N x K matrix that has the cost of building house n with color k
    start_n is the start of the subset of houses to solve for
    disallowed_color is the color (if any) not allowed for house start_n

    returns the minimum possible cost
    """

    if cache is None:
        cache = {}

    if (start_n, disallowed_color) in cache:
        return cache[(start_n, disallowed_color)]

    min_cost = None
    for k in len(costs[0]):
        if k == disallowed_color:
            continue
        cost = costs[start_n][k] 
        if start_n < len(costs)-1:
            cost += solution(costs, start_n+1, k, cache)

        if min_cost is None or cost < min_cost:
            min_cost = cost

    cache[(start_n, disallowed_color)] = min)cost
    return min_cost
    
if __name__ == "__main__":
    print()
