class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            return nums.index(target)
        
        else:
            return -1

        
        # shift = nums.index(min(nums))
        # if target in nums:
        #     shift_idx = nums.index(target)
        #     print(shift_idx)
        #     print(shift)
        #     if shift_idx < shift:
        #         return shift_idx - len(nums) + shift
            
        #     else:
        #         return shift_idx + shift
        
        # else:
        #     return -1

assert Solution().search([4,5,6,7,0,1,2], 0) == 4