class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            array_sum = sum(nums)
        
        total = 0
        for idx, pivot in enumerate(nums):
            if (array_sum - pivot) == 2 * total:
                return idx
            total += pivot
        return -1