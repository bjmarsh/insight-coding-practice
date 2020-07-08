class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        vals = [str(x) for x in preorder.split(',')]
        if len(vals)==0 or vals==["#"]:
            return True
        if vals[0]=='#':
            return False
        
        stack = [vals[0]]
        LR = ['L']
        for c in vals[1:]:
            if len(stack) == 0:
                return False
            
            if c != '#':
                stack.append(c)
                LR.append('L')
            else:
                while len(LR) > 0 and LR[-1] == 'R':
                        stack.pop()
                        LR.pop()
                if len(LR) > 0:
                    LR[-1] = 'R'
                        
        return len(stack)==0
