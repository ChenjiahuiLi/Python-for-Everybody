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
        indice = 0
        for i in range(list_num):
            current = nums[i]
            counterpart = target - current
            if current not in counterpart_dict:
                counterpart_dict[counterpart] = i
            else:
                return [counterpart_dict[current],i]
            
        