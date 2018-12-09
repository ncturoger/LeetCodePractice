class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_neg_arr = [0 for i in nums]
        max_pos_arr = [0 for i in nums]


        if nums[0] > 0:
            max_pos_arr[0] = nums[0]
        
        else:
            min_neg_arr[0] = nums[0]

        index = 1
        while index < len(nums):
            if nums[index] > 0:
                max_pos_arr[index] = max(max_pos_arr[index-1] * nums[index], nums[index])
                min_neg_arr[index] = min(min_neg_arr[index-1] * nums[index], nums[index])

            else:
                max_pos_arr[index] = max(min_neg_arr[index-1] * nums[index], nums[index])
                min_neg_arr[index] = min(max_pos_arr[index-1] * nums[index], nums[index])
            
            index += 1

        ans = max(max_pos_arr)
        if ans == 0:
            if 0 not in nums:
                return max(nums)

        return ans






assert Solution().maxProduct([2,3,-2,4]) == 6
assert Solution().maxProduct([-2,0,-1]) == 0
assert Solution().maxProduct([-2]) == -2