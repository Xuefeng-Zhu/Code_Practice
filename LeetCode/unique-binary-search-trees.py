# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        return sum(self.numTrees(x-1)*self.numTrees(n-x) for x in range(1,n+1))
        