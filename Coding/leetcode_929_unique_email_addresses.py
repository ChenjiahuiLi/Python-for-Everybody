class Solution:
    # my 1st solution
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # replace dot '.' with ''
        # keep strings between '+' and '@'
        result = []
        for email in emails:
            at_sign_index = email.find('@')
            local_name = email[:at_sign_index]
            domain_name = email[at_sign_index:]


            """
            since everything after '+' will be ignored, first deal with '+' to reduce computation
            """
            while local_name.find('+') != -1:
                plus_index = local_name.find('+')
                local_name = local_name[:plus_index]
            
            while local_name.find('.') != -1:
                dot_index = local_name.find('.')
                local_name = local_name[0:dot_index] + local_name[dot_index+1:]
                
            
                
            new_email = local_name + domain_name
            
            if new_email in result:
                next
            else:
                result.append(new_email)
                
        return(len(result))

    # A pythonic solution
    def numUniqueEmails2(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            # remove everything after the first '+'
            # if there's no '+', the following command will keep the whole string of local_name, not Error
            local_name = local_name.split('+')[0]
            # remove dot
            local_name = ''.join(local_name.split('.'))
            new_email = local_name + '@' + domain_name
            result.add(new_email)
            #print(new_email)
        """
        bug:
        if put the result.add() outside the for-loop, it will only add the LAST email into it, 
        and the length of result would forever be 1.

        below is the original code.
        """
        #result.add(new_email) 
        return(len(result))



def main():
    test1 = Solution()
    print(test1.numUniqueEmails(['find+me.da+location.id@leetcode.com','fi.nd@leetcode.com']))
    test2 = Solution()
    print(test2.numUniqueEmails2(['find+me.da+location.id@leetcode.com','fi.nd@leetcode.com','My.boss@leetcood.com']))


if __name__ == "__main__":
    main()



                
            
        