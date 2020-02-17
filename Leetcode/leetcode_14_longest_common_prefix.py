"""
The gist:
1. take out the i-th element of each string, if they are the same, i += 1
2. how to make sure i does not goes too large? min(map(len,strs))

To test with Pytest:
1. add a test_function() in the code, use `assert` to build test cases
2. ran `pytest leetcode_14_longest_common_predix.py` in command line

Put the default example use case in the main() function
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
		# 1. setup the maxium length of the LCP would be the length of the shortest string 
        # 2. for i = 0 to max_iteration - 1
        #    take out the ith character of each of the string
        #    instead of 1<>1 comparison, use a set() to store the ith char of each string
        #    in the end of every i, count the number of items in the set() object
        #    if equals 1, then it is a common prefix, added it to the returning object
        #    else, break and return the returning object
        if len(strs) < 1:
            return ""
        
		# map(function, list): equals to apply function to each element of the list, return a list
        max_iteration = min(map(len, strs))
        lcp = [] # longest common prefix
        start = 0
        
        while start < max_iteration:
            common_char = set([char[start] for char in strs])
            if len(common_char) == 1:
                lcp.append(common_char.pop()) # set.pop() remove an random element from that set and return the poped element
                start += 1
            else:
                break
                
        return ''.join(lcp)
                
                
                
def test_function():
	test1 = Solution()
	str1 = ['frequ','freq','fr']
	assert test1.longestCommonPrefix(str1) == 'fr'
	str2 = ['frequ','freq','xr']
	assert test1.longestCommonPrefix(str2) == ""
	str3 = ['frequ','freq','frequency']
	assert test1.longestCommonPrefix(str3) == "freq"
	str4 = [] # should give ""
	assert test1.longestCommonPrefix(str4) == ""
	str5 = ["a"] # should give "a"
	assert test1.longestCommonPrefix(str5) == "a"
	str6 = ["anna","anne","ab"] # should give "a"
	assert test1.longestCommonPrefix(str6) == "ab"

def main():
	test2 = Solution()
	str_list = ["anna","anne","ana"]
	print("Example string list is:")
	print(str(str_list))
	print("longest common prefix is:")
	print(test2.longestCommonPrefix(str_list))	

if __name__== "__main__":
	main()


