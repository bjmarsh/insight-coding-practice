"""
Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".
"""

def find_palindromic_substring(s):
    max_s = None
    max_len = 0
    i = 0
    while i + max_len < len(s):
        for j in range(i + max_len + 1, len(s)+1):
            ss = s[i:j]
            if ss==ss[::-1]:
                max_len = len(ss)
                max_s = ss
        i += 1
    return max_s
            
    

if __name__ == "__main__":
    print(find_palindromic_substring(""))
    print(find_palindromic_substring("abc"))
    print(find_palindromic_substring("aabcdcb"))
    print(find_palindromic_substring("bananas"))

