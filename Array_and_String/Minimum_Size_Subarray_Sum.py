class Solution(object):
    # time exceed
    def minSubArrayLen_1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums) + 1):
            idx = 0
            while idx <= len(nums)-i:
                if sum(nums[idx:idx+i]) >= s:
                    return i
                idx += 1
        return 0


    # beat 96.48 %
    def minSubArrayLen_2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        num_sum = 0
        min_length = float('inf')
        start = 0

        for idx, val in enumerate(nums):
            num_sum += val
            if num_sum >= s:
                min_length = min([min_length, idx-start+1])
                while num_sum >= s and start < idx:
                    num_sum -= nums[start]
                    if num_sum >= s:
                        min_length = min([min_length, idx-start])
                    start += 1
        
        if min_length != float('inf'):
            return min_length
        
        else:
            return 0


print(Solution().minSubArrayLen_2(7, [2,3,1,2,4,3]))

                