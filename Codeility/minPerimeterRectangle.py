from math import sqrt
def solution(N):
    result = (1 + N) * 2
    for i in range(2, int(sqrt(N))+1):
        if N % i == 0:
            result = min(result, (i + N / i) * 2)
    return result