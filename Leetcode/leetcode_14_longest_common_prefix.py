class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return('')

        result = []
        total_iteration = min(map(len, strs))     
        prefix_index = 0
        start = 1

        while start <= total_iteration:

        	prefix_set = set()



        	for string in strs:
        		i_th_char = string[prefix_index]
        		if i_th_char not in set():
        			prefix_set.add(i_th_char)

        	"""
        	Compare: whether the ith prefix in each item is the same
        	If all ith prefix are the same,
        	- increment prefix_index by 1 for next iteration 
        	- increment start by 1 to start the next iteration 

        	If not,
        	exit the While loop

        	"""

        	if len(prefix_set) == 1:
        		result.append(prefix_set.pop())
        		prefix_index += 1 
        		start += 1
        		continue
        	else:
        		break

        return(''.join(result))



def main():
	test1 = Solution()
	str1 = ['frequ','freq','fr']
	print(test1.longestCommonPrefix(str1))
	str2 = ['frequ','freq','xr']
	print(test1.longestCommonPrefix(str2))
	str3 = ['frequ','freq','frequency']
	print(test1.longestCommonPrefix(str3))
	str4 = []
	print(test1.longestCommonPrefix(str4))
	

if __name__== "__main__":
	main()


