from collections import deque
def search(i, j, m, heights):
    visited = [0] * len(heights)
    count = 0
    min = max(heights)
    d = deque()
    d.append((i,j))
    while len(d):
        x, y = d.popleft()
        if x == 0 or y == 0 or x == m -1 or y == len(heights)/m - 1:
             if heights[y * m + x] < heights[j * m + i]:
                 return 0
             else:
                continue 

        if not visited[y * m + x]:
            if heights[y * m + x] <= heights[j * m + i]:       
                visited[y * m + x] = 1
                count += 1
                
                d.append((x-1, y))
                d.append((x+1, y))
                d.append((x, y-1))
                d.append((x, y+1))
            else:
                if heights[y * m + x] < min:
                    min = heights[y * m + x]
    return count * (min - heights[j * m + i])

def rain(m, heights):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    result = 0
    for j in range(1, len(heights)/m-1):
        for i in range(1, m-1):
            result += search(i, j, m, heights)
    print result
    

if __name__ == '__main__':
    rain(3, [5, 5, 5, 5, 1, 5, 5, 5, 5])