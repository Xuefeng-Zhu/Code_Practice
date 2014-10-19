def solution(A):
    result = 0 
    count = 0 
    for i in A:
        if i == 0:
            count += 1
        else:
            result += count
            if result > 1000000000:
                return -1
    return result