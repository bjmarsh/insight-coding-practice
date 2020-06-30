class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        score = 0
        for c in s:
            if c=='1':
                score += 1
        
        maxscore = 0
        for c in s[:-1]:
            if c=='0':
                score += 1
            else:
                score -= 1
            maxscore = max(maxscore, score)
    
        return maxscore
