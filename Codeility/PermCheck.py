def solution(A):
    count = dict()
    for i in A:
        count[i] = True
    for i in range(1, len(A)+1):
        if not count.get(i):
            return 0
    return 1 