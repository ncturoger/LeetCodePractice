class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_dict = dict()
        
        for num in nums:
            if seen_dict.get(num):
                return num
            
            else:
                seen_dict[num] = True

assert Solution().findDuplicate([1,3,4,2,2]) == 2
assert Solution().findDuplicate([3,1,3,4,2]) == 3
