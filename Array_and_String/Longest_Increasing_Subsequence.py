class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_lis_list = [1 for i in nums]

        for i in range(len(nums)-1, -1, -1):
            pivot = i + 1
            max_length = 1
            while pivot < len(nums):
                if nums[i] < nums[pivot]:
                    max_length = max(max_length, max_lis_list[pivot] + 1)
                pivot += 1
            max_lis_list[i] = max_length
        
        return max(max_lis_list)


assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
