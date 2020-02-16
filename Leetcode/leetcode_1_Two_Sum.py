class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_num = len(nums)
        
        if list_num < 1:
            return False
        
        counterpart_dict = {}
        for i in range(list_num):
            current = nums[i] 
            if current not in counterpart_dict: # remember to check the current item, not the conterpart
                counterpart_dict[target - current] = i
            else:
                return [counterpart_dict[current],i]
            
        