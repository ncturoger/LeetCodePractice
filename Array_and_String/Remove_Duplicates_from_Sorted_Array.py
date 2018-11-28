class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            compare = ""
            i = 0
            while(i < len(nums)):
                if compare != nums[i]:
                    compare = nums[i]
                
                else:
                    nums.remove(nums[i])
                    i -= 1
                i += 1

        return len(nums)

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))