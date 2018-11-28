class Solution:

    # beat 5%
    def moveZeroes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                back_cursor = i 
                while back_cursor > 0 and nums[back_cursor-1] == 0:
                    temp = nums[back_cursor]
                    nums[back_cursor] = 0
                    nums[back_cursor-1] = temp
                    back_cursor -= 1
        return nums


    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0



print(Solution().moveZeroes([0,1,0,2,4,0,6]))
                    

