"""
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number 
of steps required to reach the end coordinate from the start. If there is no possible path, 
then return null. You can move up, left, down, and right. You cannot move through walls. 
You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps 
required to reach the end is 7, since we would need to go through (1, 2) 
because there is a wall everywhere else on the second row.
"""

def solution(board, start, end, seen=None, maxdist=None):
    global it
    it += 1

    if seen is None:
        seen = set()

    if maxdist is None:
        maxdist = len(board)*len(board[0])-1

    if start==end:
        return 0

    if maxdist == 0:
        return None

    row,col = start
    bestdist = None
    newseen = seen | set([start])

    for r,c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
            continue
        if (r,c) in seen:
            continue
        if board[r][c]:
            continue
        
        dist = solution(board, (r,c), end, newseen, min(bestdist-1 if bestdist is not None else maxdist, maxdist-1))
        if dist==0:
            return 1

        if bestdist is None or (dist is not None and dist < bestdist):
            bestdist = dist

    return None if bestdist is None else bestdist+1



def solution_djikstra(board, start, end):

    size = len(board)*len(board[0])
    unvisited = set()
    mindists = {}
    for r in range(len(board)):
        for c in range(len(board[0])):
            unvisited.add((r,c))
            mindists[(r,c)] = size
    unvisited.remove(start)
    mindists[start] = 0

    current = start    
    while current != end:
        row, col = current
        for r,c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
                continue
            if (r,c) not in unvisited:
                continue
            mindists[(r,c)] = min(mindists[(r,c)], mindists[current] + 1)
    
        minsite, mindist = None, size
        for r, c in unvisited:
            if board[r][c]:
                continue
            if mindists[(r,c)] < mindist:
                minsite = (r,c)
                mindist = mindists[(r,c)]

        if minsite is None or mindist==size:
            return None
        current = minsite
        unvisited.remove(current)
        
    return mindists[end]



if __name__ == "__main__":
    it = 0
    print(solution(
        [[0, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        (3, 0),
        (0, 0)
        ))
    print(it)

    print(solution_djikstra(
        [[0, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        (3, 0),
        (0, 0)
        ))

    import numpy as np
    import matplotlib.pyplot as plt
    import time

    s = None
    vals_size = []
    vals_times1 = []
    vals_times2 = []
    for dim in range(5,11):

        tot = 0
        succ = 0
        for j in range(1000):
            tot += 1
            board = (np.random.rand(dim, dim) >= 0.5).astype(int)
            board[0][0] = 0
            board[dim-1][dim-1] = 0
            s = solution_djikstra(board, (0,0), (dim-1,dim-1))
        
            if s is not None:
                succ += 1
                times1, times2 = [], []
                for k in range(10):
                    start = time.time()
                    for _ in range(10):
                        solution(board, (0,0), (dim-1, dim-1))
                    times1.append(time.time() - start)
                    start = time.time()
                    for _ in range(10):
                        solution_djikstra(board, (0,0), (dim-1, dim-1))
                    times2.append(time.time() - start)
                vals_size.append(dim)
                vals_times1.append(np.amin(times1))
                vals_times2.append(np.amin(times2))

        print(dim, succ/tot)

    plt.scatter(vals_size, vals_times1, alpha=0.4)
    plt.scatter(np.array(vals_size)+0.1, vals_times2, alpha=0.4)
    plt.gca().set_yscale('log')
    plt.show()
