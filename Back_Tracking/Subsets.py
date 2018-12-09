class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.find_sub(nums, 0)
    
    def find_sub(self, nums, pivot):
        ans = []
        if pivot == len(nums) - 1:
            ans.append([nums[pivot]])
            ans.append([]) 
            return ans
        
        
        for sub in self.find_sub(nums, pivot + 1):
            ans.append([nums[pivot]] + sub)
            ans.append(sub)
        
        return ans
        


assert Solution().subsets([1,2,3]) == [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]