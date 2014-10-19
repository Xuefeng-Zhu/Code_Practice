def solution(X, A):
    bitmap = {}
    count = 0
    for i in A:
        if not bitmap.get(i):
            bitmap[i] = True
            count += 1
            if count == X:
                return A.index(i)
    return -1