class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        vals = {c:i for i,c in enumerate(order)}
        
        def comp(w1, w2):
            """ returns true if w1 < w2 alphabetically """
            for i,c in enumerate(w1):
                if i >= len(w2):
                    return False
                if vals[c] < vals[w2[i]]:
                    return True
                if vals[c] > vals[w2[i]]:
                    return False
            return True
        
        for i in range(len(words)-1):
            if not comp(words[i], words[i+1]):
                return False
        
        return True
        
