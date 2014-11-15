# Given an array of integer numbers print to the standard output the nth circular permutation to the right.
# Expected complexity: O(N)
# The first 4 permutations to the right for the 7 1 2 array are: 2 7 1 -> 1 2 7 -> 7 1 2 -> 2 7 1

def nth_perm(v, n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    for i in range(len(v)):
        print v[(i - n) % len(v)]

