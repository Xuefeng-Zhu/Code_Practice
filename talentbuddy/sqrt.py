def compute_sqrt(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    low = 0
    high = n 
    while low != high:
        mid = (low + high) / 2 
        tmp = mid * mid
        if tmp == n or mid == low:
            low = mid
            break
        elif tmp < n:
            low = mid 
        else:
            high = mid
    print low

if __name__ == '__main__':
    compute_sqrt(17)