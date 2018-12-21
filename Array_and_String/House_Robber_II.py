class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.house_rob(nums[:-1]), self.house_rob(nums[1:]))

    def house_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check money[i] = max(money[i-1], money[i-2] + nums[i])
        if not nums:
            return 0
        
        max_money = [0 for i in nums]
        i = 0
        while i < len(nums):
            if i == 0:
                max_money[i] = nums[i]
            
            elif i == 1:
                max_money[1] = max(nums[i-1], nums[i])

            else:
                max_money[i] = max(max_money[i-1], max_money[i-2] + nums[i])
            i += 1
        
        return max(max_money)

assert Solution().rob([2,3,2]) == 3
assert Solution().rob([1,2,3,1]) == 4
assert Solution().rob([2,1,1,1]) == 3
assert Solution().rob([2,1,1,2]) == 3
assert Solution().rob([2]) == 2