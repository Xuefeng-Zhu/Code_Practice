def moveforward(v, i, j):
    while j > i:
        if v[j-1] < 0:
            moveforward(v, i, j-1)
            i += 1
        else:
            v[j-1], v[j] = v[j], v[j-1]
            j -= 1

def relative_sort(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    i = 0 
    j = len(v)-1
    while i < j:
        while v[i] < 0:
            i += 1 
        while v[j] > 0:
            j -= 1
        if i < j:
            moveforward(v, i, j)
    print v

if __name__ == '__main__':
    relative_sort([49, 43, 38, -47, 48, 44, 64, -32, 27, 53, 58, 41, -21, -5, -50, -26, -31, 22, 30, 54, 61, -57, -9, 6, 18, 68, 66, -17, -24, 7, 70, -11, -28, -51, -63, 65, 45, 42, 10, -35, 56, -36, -37, 39, -4, -15, 23, 3, 20, 12, -55, -1, 40, -52, -14, 19, 60, 59, 46, -25, 8, 67, -62, -34, -29, 13, -16, 2, 33, 69])