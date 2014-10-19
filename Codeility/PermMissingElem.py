def solution(A):
    N = len(A)
    total = (1 + N + 1) * (N + 1) / 2
    for i in A:
        total -= i
    return total