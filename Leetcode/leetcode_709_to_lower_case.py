class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = []
        
        for char in str:
            """
            ord('a') = 97
            ord('A') = 65
            ord('z') = 122
            ord('Z') = 90
            chr(97) = 'a'
            """
            if ord(char) >= 65 and ord(char) <= 90:
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
                
        return(''.join(result))
                
            
        