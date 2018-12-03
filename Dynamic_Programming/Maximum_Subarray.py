class Solution(object):
    # Time Limit Exceeded
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for idx, val in enumerate(nums):
            j = 0
            while (idx + j) < len(nums):
                max_sum = max(sum(nums[idx: idx + j + 1]), max_sum)
                j += 1
        return max_sum

    
    def maxSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = acc_val = nums[0]
        for i in nums[1:]:
            acc_val = max(i, acc_val + i)
            max_val = max(max_val, acc_val)
        return max_val