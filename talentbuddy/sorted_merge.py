def merge_arrays(a, b):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    i = 0
    j = 0 
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result += a[i:]
    else:
        result += b[j:]
    for i in result:
        print i 
    

