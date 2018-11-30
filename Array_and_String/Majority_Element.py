class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        threshold = int(len(nums)/2)
        for num in num_set:
            if nums.count(num) > threshold:
                return num
