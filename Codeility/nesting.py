def solution(S):
    count = 0
    for i in S:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return 0
            count -= 1
    return 1 if count == 0 else 0
