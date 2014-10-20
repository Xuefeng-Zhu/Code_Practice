def solution(A):
    leader = None
    count = 0
    for i in A:
        if count == 0:
            count += 1
            leader = i
        else:
            if leader == i:
                count += 1
            else:
                count -= 1
    if count > 0 and A.count(leader)>len(A)/2:
        result = []
        for i in range(len(A)):
            if A[i] == leader:
                return i
    else:
        return -1
