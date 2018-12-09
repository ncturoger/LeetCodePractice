class Solution():
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.create_permute(nums)

    def create_permute(self, nums):
        perm_list = []
        if len(nums) == 1:
            perm_list.append(nums)
            return perm_list

        for idx, num in enumerate(nums):
            for item in self.create_permute(nums[:idx] + nums[idx+1:]):
                perm_list.append([num] + item)
        
        return perm_list
    


assert Solution().permute([1,2,3]) == [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]