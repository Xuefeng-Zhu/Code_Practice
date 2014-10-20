def solution(A):
    if (len(A)==0):
        return 0
    result = 0
    low = A[0]
    high = A[0]
    for i in A:
        if i < low:
            low = i
            high = low
        if i > high:
            high = i
            result = max(result, high -low)
    return result 