"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random

def rand5():
    return random.randint(1,5) 

def rand7():
    
    r = 8
    while r > 7:
        x1, x2 = rand5(), rand5()
        r = 5*(x1-1) + (x2-1)
        r = r//3 + 1

    return r
    

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    rs = [rand7() for _ in range(10000)]
    plt.hist(rs, bins=range(10))
    plt.show()


