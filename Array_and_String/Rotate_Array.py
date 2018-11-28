class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            arr_len = len(nums)
            tem = nums[arr_len-1]
            del nums[arr_len-1]
            nums.insert(0, tem)