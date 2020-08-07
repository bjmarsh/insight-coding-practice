"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""

import random

def estimate_pi(tol=0.001):
    """
    Estimate pi with an uncertainty of no more than tol

    This is done by randomly generating points in the unit square,
    and finding the fraction p that lie within the inscribed circle.
    The square has area 1 and the circle area pi/4, so pi ~ 4*p
    
    The uncertainty on p can be estimated with the formula for a binomial proportion:
      dp = sqrt(p*(1-p) / N),
    where N is the number of samples.
    We want 4*dp to have an upper bound of tol. We can use p=0.5 to get an upper bound.
      N = 0.25 / (tol/4)^2
    """

    N = int(0.25 / (tol/4)**2)
    num, den = 0, N
    for i in range(N):
        x = random.random() - 0.5
        y = random.random() - 0.5
        if x**2 + y**2 < 0.25:
            num += 1
    p = num/den

    return 4*p

    

if __name__ == "__main__":
    print(estimate_pi(0.001)) 

    import numpy as np
    vals = []
    for i in range(20):
        vals.append(estimate_pi(0.001))
    print(np.std(vals))
