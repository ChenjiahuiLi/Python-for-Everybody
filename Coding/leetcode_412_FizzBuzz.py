def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        if n <= 0:
            return([])
        
        i = 1
        while i <= n:
            if i % 3 != 0 and i % 5 != 0:
                result.append(str(i))
            else:
                if i % 15 == 0:
                    result.append('FizzBuzz')
                elif i % 3 == 0:
                    result.append('Fizz')
                else:
                    result.append('Buzz')
            
            i = i + 1
            
        return(result)

# More Pythonic solution
def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [('Fizz' if (i+1) % 3 == 0 else '') + \
              ('Buzz' if (i+1) % 5 == 0 else '') + \
              (str(i+1) if not ((i+1) % 3 == 0 or (i+1) % 5 == 0) else '')  \
              for i in list(range(n))]
            
        return(result)
        