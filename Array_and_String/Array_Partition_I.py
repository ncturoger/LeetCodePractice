class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pair_sum = 0
        for i in range(0, len(nums), 2):
            pair_sum += min(nums[i], nums[i+1])
        
        return pair_sum


print(Solution().arrayPairSum([1,4,3,2]))
