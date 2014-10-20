def solution(H):
    stack = []
    count = 0 
    for i in H:
        if len(stack) == 0 or stack[-1] < i:
            stack.append(i)
            count += 1
        elif stack[-1] > i:
            while len(stack) and stack[-1] > i:
                stack.pop()
            if len(stack) == 0 or stack[-1] < i:
                stack.append(i)
                count += 1
    return count 
            