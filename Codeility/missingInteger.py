def solution(A):
    bitmap = {}
    maxNum = 0
    for i in A:
        bitmap[i] = True
        maxNum = max(i, maxNum)
    for i in range(1, len(A)+1):
        if not bitmap.get(i):
            return i
    return maxNum + 1