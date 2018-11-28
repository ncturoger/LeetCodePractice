class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for item in nums:
            if item == 1:
                count += 1

            else:
                count = 0

            if max_count < count:
                max_count = count
        return max_count