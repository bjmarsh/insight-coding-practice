"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

import random

def rand(k):
    return random.randint(1, k)


def shuffle(vals):
    for i in range(len(vals)):
        j = i + rand(len(vals)-i) - 1
        vals[i], vals[j] = vals[j], vals[i]
    return vals

if __name__ == "__main__":
    import numpy as np
    N = 10
    counts = np.zeros((N,N))
    for i in range(100000):
        vals = list(range(10))
        shuffle(vals)
        for i in range(len(vals)):
            counts[i, vals[i]] += 1

    import matplotlib.pyplot as plt
    plt.imshow(counts)
    plt.colorbar()
    plt.show()
        


