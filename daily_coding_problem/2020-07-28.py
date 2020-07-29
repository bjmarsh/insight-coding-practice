"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) return the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given the below implementation of cons, implement car and cdr
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a,b: a)

def cdr(pair):
    return pair(lambda a,b: b)

if __name__ == "__main__":
    print(car(cons(3,4)))
    print(cdr(cons(3,4)))
    print(car(cons(9,8)))
    print(cdr(cons(9,8)))

