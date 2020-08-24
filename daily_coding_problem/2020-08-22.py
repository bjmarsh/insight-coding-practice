"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to 
represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded 
have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""

def encode(s: str) -> str:
    istart = 0
    enc = ""
    while istart < len(s):
        iend = istart
        while iend < len(s) and s[iend] == s[istart]:
            iend += 1
        enc += str(iend-istart) + s[istart]
        istart = iend
    return enc

def decode(s: str) -> str:
    dec = ""
    istart = 0
    dig = set(list('0123456789'))
    while istart < len(s):
        iend = istart
        while s[iend] in dig:
            iend += 1
        n = int(s[istart:iend])
        dec += s[iend] * n
        istart = iend+1
    return dec

if __name__ == "__main__":
    print(encode("AAAABBBCCDAA"))
    print(decode(encode("AAAABBBCCDAA")))
    print(decode("4A10B1C"))

