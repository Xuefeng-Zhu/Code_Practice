# Given an array of integers, every element appears three times except for one. Find that single one.

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return  (3*sum(set(A)) - sum(A)) / 2