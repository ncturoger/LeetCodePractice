class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        nums = set(nums)
        check = set([i for i in range(1, nums_len + 1)])

        return list(check - nums)