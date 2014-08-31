# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


def twoSum(num, target):
        search = {}
        for i in range(len(num)):
            if (search.get(num[i])):
                return (search.get(num[i]), i+1)
            search[target-num[i]] = i + 1


if __name__ == '__main__':
	print twoSum([2,7,11,15], 9)