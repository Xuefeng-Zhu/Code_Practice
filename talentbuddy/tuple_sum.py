def search(a, index, s, deep):
    if deep == 0:
        for i in range(index, len(a)):
            if a[i] == s:
                return [i]
        return False
    result = search(a, index + 1, s-a[index], deep-1)
    if result:
        return [index] + result
    else:
        if len(a) - index - 1 > deep:  
            return search(a, index + 1, s, deep)
        else:
            return False 
def tuple_sum(a, s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    result = search(a, 0, s, 3)
    if not result:
        print 0
    
    for i in result:
        print i


if __name__ == '__main__':
    tuple_sum([3, 2, 1, 4, 5, 7, 6, 9, 8], 30)