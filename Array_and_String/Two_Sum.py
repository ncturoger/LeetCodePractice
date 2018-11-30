class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, val in enumerate(nums):
            find = target - val
            nums[idx] = None
            if find in nums:
                return [idx, nums.index(find)]


print(Solution().twoSum([3,2,4], 6))