# Given a string S, find the longest palindromic substring in S.

def expand_string(s, i, j):
	if i < 0 or j == len(s):
		return s[i+1:j]
	if s[i] == s[j]:
		return expand_string(s, i-1, j+1)
	else:
		return s[i+1:j]

if __name__ == '__main__':
	long_str = raw_input("Please input the string\n")
	longest_sub = ""
	for i in range(len(long_str)):
		temp = expand_string(long_str, i, i)
		if len(temp) > len(longest_sub):
			longest_sub = temp
		temp = expand_string(long_str, i, i+1)
		if (len(temp) > len(longest_sub)):
			longest_sub = temp

	print longest_sub


