"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def n_possible_decodings(encoding: str) -> int:
    
    # if string is empty, there is one (trivial) decoding
    if len(encoding) == 0:
        return 1
    # if the string starts with a 0, there are no possible decodings
    if encoding[0] == '0':
        return 0

    n_possible = 0

    # the first digit can be mapped to one of the first 9 letters
    n_possible += n_possible_decodings(encoding[1:])

    # if the first two digits are <=26, then we can combine them into a single letter
    if len(encoding) >= 2 and int(encoding[:2]) <= 26:
        n_possible += n_possible_decodings(encoding[2:])

    return n_possible

if __name__ == "__main__":
    print(n_possible_decodings('111'))


