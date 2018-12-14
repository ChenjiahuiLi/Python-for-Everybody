class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        
        # Double Pointer
        left = 0
        right = len(s) - 1
        
        result = ['#'] * (right+1)
        
        while left <= right:
            if s[left] not in vowels:
                result[left] = s[left]
                left += 1       
                # in case len(s) is a odd number, left += 1 will let left == right
                # then the current right index string will not be written in to the list
                # if the while condition is : left < right
            else:
                if s[right] not in vowels:
                    result[right] = s[right]
                    right -= 1
                else:
                    result[left] = s[right]
                    result[right] = s[left]
                    left += 1
                    right -= 1
                            
        return(''.join(result))

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u', 'A','E','I','O','U']
        
        # Double Pointer
        left = 0
        right = len(s) - 1
        
        result = ['#'] * (right+1)
        
        while left < right:
            if s[left] not in vowels:
                result[left] = s[left]
                left += 1       
                # in case len(s) is a odd number, left += 1 will let left == right
                # then the current right index string will not be written in to the list
                # if the while condition is : left < right
            else:
                if s[right] not in vowels:
                    result[right] = s[right]
                    right -= 1
                else:
                    result[left] = s[right]
                    result[right] = s[left]
                    left += 1
                    right -= 1
                            
        return(''.join(result))
    
 
def main():
    t1 = Solution()
    print(t1.reverseVowels('hello'))
    print(t1.reverseVowels2('hello'))

if __name__ == "__main__":
    main()
