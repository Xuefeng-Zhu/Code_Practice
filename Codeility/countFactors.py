from math import sqrt, ceil
def solution(N):
    return len([i for i in range(1, int(ceil(sqrt(N)))) if N % i == 0]) * 2 + (1 if sqrt(N) == int(sqrt(N)) else 0)
