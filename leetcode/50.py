class Solution:
    def primeFactor(self, n):
        pfs = []
        d = 2
        while n > 1 and d*d <= n:
            while n%d == 0:
                pfs.append(d)
                n //= d
            d += 1 if d==2 else 2
        if n > 1:
            pfs.append(n)
        return pfs
        
        
    def myPow(self, x: float, n: int) -> float:
        
        # print(self.primeFactor(2147483647))
        # return 0
        
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1.0/x
        
        sgn = 1 if n>0 else -1
        
        n *= sgn
        pfs = self.primeFactor(n)
        # print(pfs)
        if len(pfs)==1:
            x *= self.myPow(x, n-1)
        else:
            for p in pfs:
                # print(p,x)
                y = x
                for i in range(p-1):
                    x *= y
                    if x==0:
                        return 0
        
        return x if sgn>0 else 1.0/x
