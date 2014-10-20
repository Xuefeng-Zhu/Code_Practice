def solution(S):
    d = {')':'(', '}':'{', ']':'['}
    stack = []
    for c in S:
        if c in "({[":
            stack.append(c)
        else:
            if len(stack) == 0 or d[c] != stack.pop():
                return 0
    return 1 if len(stack) == 0 else 0