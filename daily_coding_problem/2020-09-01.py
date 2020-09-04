"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list 
of live cell coordinates and the number of steps it should run for. Once initialized, 
it should print out the board state at each step. Since it's an infinite board, 
print out only the relevant coordinates, i.e. from the top-leftmost live cell to 
bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""


class GameOfLife:
    def __init__(self, live_coords):
        self.live_rows = {}
        self.min_row, self.max_row = float('inf'), float('-inf')
        self.min_col, self.max_col = float('inf'), float('-inf')
        for r,c in live_coords:
            if r not in self.live_rows:
                self.live_rows[r] = set()
            self.live_rows[r].add(c)

            self.min_row = min(self.min_row, r)
            self.max_row = max(self.max_row, r)
            self.min_col = min(self.min_col, c)
            self.max_col = max(self.max_col, c)

    def is_live(self, r, c):
        if r not in self.live_rows:
            return False
        if c not in self.live_rows[r]:
            return False
        return True

    def n_live_neighbors(self, r, c):
        nlive = 0
        for ir in range(r-1,r+2):
            for ic in range(c-1, c+2):
                if ir==r and ic==c:
                    continue
                if self.is_live(ir,ic):
                    nlive += 1
        return nlive

    def adv_one_step(self):
        if self.min_row == float('inf'):
            # empty board, do nothing
            return

        tmp_live_rows = {r: set(self.live_rows[r]) for r in self.live_rows}
        for r in range(self.min_row-1, self.max_row+2):
            for c in range(self.min_col-1, self.max_col+2):
                nlive = self.n_live_neighbors(r,c)
                if self.is_live(r,c):
                    if nlive < 2 or nlive > 3:
                        tmp_live_rows[r].remove(c)
                else:
                    if nlive == 3:
                        if r not in tmp_live_rows:
                            tmp_live_rows[r] = set()
                        tmp_live_rows[r].add(c)

        self.live_rows = {r: set(tmp_live_rows[r]) for r in tmp_live_rows if tmp_live_rows[r]}
        self.min_row, self.max_row = float('inf'), float('-inf')
        self.min_col, self.max_col = float('inf'), float('-inf')
        for r in self.live_rows:
            self.min_row = min(self.min_row, r)
            self.max_row = max(self.max_row, r)
            for c in self.live_rows[r]:
                self.min_col = min(self.min_col, c)
                self.max_col = max(self.max_col, c)

    def __repr__(self):
        if self.min_col == float('inf'):
            return "Empty"
        s = ""
        s += "{0},{1}\n{2},{3}\n".format(self.min_row, self.max_row, self.min_col, self.max_col)
        ncols = self.max_col - self.min_col + 1
        for r in range(self.min_row, self.max_row + 1):
            if r not in self.live_rows:
                s += '-' * ncols
            else:
                for c in range(self.min_col, self.max_col+1):
                    if c in self.live_rows[r]:
                        s += '#'
                    else:
                        s += '-'
            s += '\n'
        return s

# def adv_one_step(board):
    
if __name__ == "__main__":
    # g = GameOfLife([(0,0),(0,1),(0,2),(2,1)])

    # R-pentomino
    # g = GameOfLife([(0,0),(0,1),(-1,1),(1,1),(-1,2)])
    # Diehard
    # g = GameOfLife([(0,0),(0,1),(1,1),(1,5),(1,6),(1,7),(-1,6)])
    # Acorn
    g = GameOfLife([(0,0),(0,1),(-2,1),(-1,3),(0,4),(0,5),(0,6)])
    
    print(g)
    while True:
        input()
        g.adv_one_step()
        print(g)
        
