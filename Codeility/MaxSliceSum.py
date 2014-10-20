def solution(A):
    result = -2147483648
    total = 0
    for i in A:
        total = max(i, total + i)
        result = max(total, result)
    return result