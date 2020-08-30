"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""

def generate_power_set(vals, used=None):
    if not isinstance(vals, set):
        vals = set(vals)

    if used is None:
        used = set()

    power_set = [set()]
    for x in vals - used:
        used = used | set([x])
        for subset in generate_power_set(vals, used):
            power_set.append(subset | set([x]))

    return power_set
    

if __name__ == "__main__":
    print(generate_power_set([]))
    print(generate_power_set([1]))
    print(generate_power_set([1,2]))
    print(generate_power_set([1,2,3]))
    print(generate_power_set([1,2,3,4]))

