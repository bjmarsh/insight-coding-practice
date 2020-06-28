
def bubble_sort(vals, inplace=False):
    if not inplace:
        vals = list(vals)
    size = len(vals)
    
    nflips = 1
    iter = 0
    while nflips > 0:
        nflips = 0
        iter += 1
        for i in range(size-iter):
            if vals[i+1] < vals[i]:
                vals[i], vals[i+1] = vals[i+1], vals[i]
                nflips += 1

    return vals


def selection_sort(vals, inplace=False):
    if not inplace:
        vals = list(vals)
    size = len(vals)
    
    for istart in range(size-1):
        min_idx, min_val = istart, vals[istart]
        for j in range(istart+1, size):
            if vals[j] < min_val:
                min_idx, min_val = j, vals[j]
        vals[istart], vals[min_idx] = vals[min_idx], vals[istart]

    return vals


def insertion_sort(vals):
    size = len(vals)

    ret = [vals[0]]
    for cur in range(1, size):
        x = vals[cur]
        i = 0
        while i < cur and x >= ret[i]:
            i += 1
        ret.insert(i, x)
    
    return ret

def merge_sort(vals, lo=0, hi=-1, inplace=False):
    if not inplace:
        vals = list(vals)
    size = len(vals)
    if hi == -1:
        hi = size-1

    def merge(l1, l2):
        """ merge two sorted lists l1, l2 """
        merged = []
        i1, i2 = 0, 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                merged.append(l1[i1])
                i1 += 1
            else:
                merged.append(l2[i2])
                i2 += 1
        if i1 < len(l1):
            merged.extend(l1[i1:])
        if i2 < len(l2):
            merged.extend(l2[i2:])
        return merged

    if hi-lo+1 < 2:
        return vals
    idx = (lo+hi+1) // 2

    merge_sort(vals, lo, idx-1, inplace=True)
    merge_sort(vals, idx, hi, inplace=True)
    vals[lo:hi+1] =  merge(vals[lo:idx], vals[idx:hi+1])

    return vals


def quick_sort(vals, lo=0, hi=-1, inplace=False):
    if not inplace:
        vals = list(vals)
    size = len(vals)

    if hi == -1:
        hi = size-1

    if hi-lo+1 < 2:
        return vals

    pivot = vals[hi]
    i = lo
    for j in range(lo, hi+1):
        if vals[j] < pivot:
            vals[i], vals[j] = vals[j], vals[i]
            i += 1
    vals[i], vals[hi] = vals[hi], vals[i]

    quick_sort(vals, lo, i-1, inplace=True)
    quick_sort(vals, i+1, hi, inplace=True)

    return vals



if __name__ == "__main__":
    import numpy as np
    print(merge_sort(np.random.randint(1,100, 10)))
