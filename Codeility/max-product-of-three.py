def solution(A):
    A.sort()
    return A[-1] * (max(A[-2] * A[-3], A[0] * A[1]) if A[-1]>0 else min(A[-2] * A[-3], A[0] * A[1]))
