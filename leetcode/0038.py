class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s1 = "1"
        for it in range(n-1):
            s2 = []
            i = 0
            while i < len(s1):
                j = i
                while j<len(s1) and s1[j]==s1[i]:
                    j += 1
                s2.append(str(j-i))
                s2.append(s1[i])
                i = j
            s1 = ''.join(s2)
        
            
        return s1
