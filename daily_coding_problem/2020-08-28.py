"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the 
array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def solution(vals):

    r_pointer = 0
    b_pointer =  len(vals) - 1
    i = 0
    count = 0
    while i <= b_pointer:
        count += 1

        if vals[i] == 'G':
            i += 1
        elif vals[i] == 'R':
            vals[r_pointer], vals[i] = vals[i], vals[r_pointer]
            r_pointer += 1
        else:
            vals[b_pointer], vals[i] = vals[i], vals[b_pointer]
            b_pointer -= 1

        i = max(i, r_pointer)

    return vals, count


def verify(vals):
    
    seen_g = False
    seen_b = False
    for c in vals:
        if c== 'G':
            seen_g = True
        if c=='B':
            seen_b = True

        if c=='R' and (seen_g or seen_b):
            return False
        if c=='G' and seen_b:
            return False

    return True


if __name__ == "__main__":
    # print(solution(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

    import random
    print(solution(["RGB"[random.randint(0,2)] for i in range(20)]))

    import matplotlib.pyplot as plt

    xs = []
    ys = []
    for size in range(5, 100):
        for i in range(10):
            vals, count = solution(["RGB"[random.randint(0,2)] for i in range(size)])
            assert verify(vals)
            xs.append(size)
            ys.append(count)

    plt.scatter(xs, ys, alpha=0.4)
    plt.show()
