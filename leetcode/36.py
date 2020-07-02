class Solution(object):
    from collections import defaultdict
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        def valid_set(nums):
            counts = defaultdict(int)
            for c in nums:
                if c=='.':
                    continue
                counts[c] += 1
                if counts[c] > 1:
                    return False
            return True
        
        
        for i in range(9):
            
            # check rows
            if not valid_set(board[i]):
                return False
            
            # check cols
            if not valid_set([board[j][i] for j in range(9)]):
                return False
            
            # check boxes
            ir = i//3
            ic = i%3
            vals = []
            for irow in range(3*ir, 3*ir+3):
                vals.extend(board[irow][ic*3:ic*3+3])
            if not valid_set(vals):
                return False
        
        return True
        
        
