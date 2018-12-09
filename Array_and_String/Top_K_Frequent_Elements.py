class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_set = set(nums)
        freq_tup = []
        for num in nums_set:
            freq_tup.append((nums.count(num), num))
        
        freq_tup.sort()
        return [i[1]  for i in freq_tup[-1:-k-1:-1]]



assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert Solution().topKFrequent([1], 1) == [1]