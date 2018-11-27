class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = max(nums)
        twice_nums = [item * 2 for item in nums if item != max_value]
        for item in twice_nums:
            if max_value < item:
                return -1
        return nums.index(max_value)

