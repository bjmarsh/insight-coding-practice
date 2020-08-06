"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def solution(k: int, s: str) -> int:
    """ find the length of the longest substring of s that contains at most k distinct characters """

    # brute-force-ish, worst case O(n^2), best case O(n)
    
    longest = 0
    for istart in range(len(s)):
        iend = istart + longest
        if iend >= len(s):
            break
        chars = set(list(s[istart:iend+1]))
        while iend < len(s) and len(chars) <= k:
            longest = iend - istart + 1
            iend += 1
            if iend < len(s):
                chars.add(s[iend])

    return longest


if __name__ == "__main__":
    print(solution(2, "abcba")) # 3
    print(solution(2, "aaaaa")) # 5 (worst case)
    print(solution(5, "abcde")) # 5 (best case)
