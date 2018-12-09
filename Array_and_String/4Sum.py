class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set([])
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                need = target - nums[j] - nums[i]
                forward = j + 1
                back = len(nums) - 1
                while forward < back:
                    total = nums[forward] + nums[back]
                    if total == need:
                        result.add([nums[i], nums[j], nums[forward], nums[back]])
                        forward += 1
                        back -= 1

                    elif total < need:
                        forward += 1
                    
                    elif total > need:
                        back -= 1
        return [item for item in result]