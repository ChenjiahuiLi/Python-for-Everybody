class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        """
        Think of [x,y] represent a single block in a 7 by 7 matrix A,
        if we draw x and y from Rand7(), then [x, y] is equally likely
        to be in each block on the matrix A.
        
        If we make the 7 by 7 matrix A into a 1 by 49 row vector B, the row
        index of [x,y] in the new vector would be x + (y-1)*7. 
        
        While x + (y-1)*7 can draw integers uniformly from range(1,49). 
        
        Since range(1,49) covers 5 times of 1~9 but 4 times of 0, we abandon 
        41 to 49 from the possible set of x + (y-1)*7, so that each integer
        from 0 to 9 are equally likely to be generated.
                
        """
        row = rand7()
        col = rand7()
        idx = col + (row-1)*7
        
        if idx > 40: 
            return(self.rand10())
        else:
            return(idx % 10 + 1)

        
        
            
        
        
        
        
