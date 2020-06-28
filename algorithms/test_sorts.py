from collections import defaultdict
import time
import numpy as np
import matplotlib.pyplot as plt

from sorting_functions import *

def test_sort(fnc, nlists=1, listsize=1000, navg=1, seed=None):
    if seed:
        np.random.seed(seed)
    times = []
    for ilist in range(nlists):
        vals = np.random.randint(0, 1000000, listsize)
        ts = []
        for j in range(navg):
            start_time = time.time()
            fnc(vals)
            ts.append((time.time()-start_time))
        times.append(np.amin(ts))
        
    return times

if __name__ == "__main__":
    fncs = {
        "builtin": sorted, 
        "bubble" : bubble_sort,
        "selection" : selection_sort,
        "insertion" : insertion_sort,
        "merge" : merge_sort,
        # "quick" : quick_sort,
    }
    

    xs = defaultdict(list)
    ys = defaultdict(list)
    nlists = 1
    navg = 10

    for name,fnc in fncs.items():
        for listsize in np.logspace(1.7, 3.3, 20):            
            times = test_sort(fnc, nlists=nlists, navg=navg, listsize=int(listsize), seed=int(listsize))
            xs[name].extend([listsize]*nlists)
            ys[name].extend(times)

        plt.scatter(xs[name], ys[name], label=name, s=10)

    plt.legend(loc='upper left')
    plt.gca().set_xscale('log')
    plt.gca().set_yscale('log')
    plt.show()
    
