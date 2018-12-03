class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        origin = [item for item in nums]
        nums.sort()
        sorted_arr = nums
        count = 0
        start = None
        end = None
        for idx, item in enumerate(origin):
            if item != sorted_arr[idx]:
                if start is None:
                    start = idx
                
                else:
                    end = idx
                
        
        if end is not None and start is not None:
            return end - start + 1
        
        if end is None and start is not None:
            return 1

        if end is None and start is None:
            return 0


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
