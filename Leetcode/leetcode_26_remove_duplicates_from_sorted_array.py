class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        l = 0
        r = 1
        
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
                
            else:
                l += 1
                r += 1
        return(len(nums))
        
def test_functions():
    test = Solution()
    assert test.removeDuplicates([1,1,2]) == 2
    assert test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
    assert test.removeDuplicates([0]) == 1