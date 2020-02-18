class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mappings = {"{":"}","[":"]","(":")"}
        stack = []
        
        # if the string contains odd number of characters, then it must not be valid
        if len(s) % 2!= 0:
            return False

        for p in s:
            if p in mappings:
                stack.append(p)
            else:
                if not stack:
                    return(False)
                else:
                    top = stack.pop()
                    """
                    think about: "([)]", 
                    the new p should match with the right most element
                    in the stack.
                    so it should be:
                    top = stack.pop(-1)
                    rather than
                    top = stack.pop(0)
                
                    """
                    if mappings[top] != p:
                        return(False)
        
        if stack:
            return(False)
        else:
            return(True)

def main():

    t1 = Solution()
    print(t1.isValid("()")) 

    t2 = Solution()
    print(t2.isValid("{{}[][[[]]]}"))


    t3 = Solution()
    print(t3.isValid("(]"))


    t4 = Solution()
    print(t4.isValid("([)]"))

if __name__ == '__main__':
	main()


def test_functions():
    test = Solution()
    assert test.isValid("]") == False
    assert test.isValid("[") == False
    assert test.isValid("()[]{}") == True
    assert test.isValid("))") == False
    assert test.isValid("}(") == False

    	
                
        


