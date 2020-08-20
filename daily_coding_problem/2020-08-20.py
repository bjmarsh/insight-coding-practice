"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def solution(s: str) -> bool:
    
    left = set(list('([{'))
    
    match = {')':'(', ']':'[', '}':'{'}

    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        else:
            if len(stack) > 0 and stack[-1] == match[c]:
                stack.pop()
            else:
                return False
    
    return len(stack)==0

    
if __name__ == "__main__":
    print(solution("([])[]({})"))
    print(solution("([)]"))
    print(solution("((()"))

