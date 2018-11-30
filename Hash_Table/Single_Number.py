class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = set(nums)

        for item in target:
            nums.remove(item)
        
        diff = target - set(nums)

        return diff.pop()
print(Solution().singleNumber([2,2,1]))