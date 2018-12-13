
# My First Solution
class Solution:
    def str2dict(self, s):
            output = {}           
            for i in list(range(len(s))):
                if s[i] in output:
                    output[s[i]] += 1
                else:
                    output[s[i]] = 1
            return(output)
        
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        
        stones = self.str2dict(S)
                
        common = 0
        
        for key, value in stones: # wrong: stones is a dicitonary, to retrieve both key and value, stones should be stones.item()
            if key in J:
                common += value
                
        return(common)

# Pass Solution
class Solution:
    
    # define str2dict(self,s) as a method of Solution class, it is callable via self.str2dict(string)
    def str2dict(self, s):
            output = {}           
            for i in list(range(len(s))):
                if s[i] in output:
                    output[s[i]] += 1
                else:
                    output[s[i]] = 1
            return(output)
        
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """        
        stones = self.str2dict(S)
                
        common = 0
        
        for key, value in stones.items(): 
            if key in J:
                common += value
                
        return(common)

# Or a one liner using map() and count()
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """    
        # the one liner solution
        # return(sum(map(S.count, J)))
        # Breakdown
        # for every character in J, count the number of occurance in S
        tmp = map(S.count, J)
        # gives a map object: <map object at 0x10a76f7f0>
        # we can list the occurance
        res = list(tmp)
        # or we could sum up the occurances directly 
        return(sum(tmp))
        
        