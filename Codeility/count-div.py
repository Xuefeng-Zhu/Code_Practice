def solution(A, B, K):
    mod = A % K
    diff = B - A
    if mod:
        diff -= K - mod
    if diff < 0:
        return 0
    else:
        return diff / K + 1