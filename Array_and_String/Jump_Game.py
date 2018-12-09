class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1
        pivot = len(nums) - 2
        walked = target
        isDeadEnd = False

        while pivot > -1:
            isDeadEnd = True
            if walked - pivot <= nums[pivot]:
                isDeadEnd = False
                walked = pivot
            pivot -= 1
        
        return not isDeadEnd


assert Solution().canJump([2,3,1,1,4]) == True
assert Solution().canJump([3,2,1,0,4]) == False
assert Solution().canJump([3,2,2,0,4]) == True
assert Solution().canJump([0,2,3]) == False


