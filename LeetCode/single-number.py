# Given an array of integers, every element appears twice except for one. Find that single one
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce((lambda a, b: a ^ b), A)
        