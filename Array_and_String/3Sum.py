class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        checked_set = set()
        ans_dict = dict()

        for idx, item in enumerate(nums):
            if item not in checked_set:
                target = - item
                forward_idx = idx + 1
                back_idx = len(nums) - 1
                while forward_idx < back_idx:
                    if nums[forward_idx] + nums[back_idx] == target:
                        if not ans_dict.get([item, nums[forward_idx], nums[back_idx]]):
                            ans.append([item, nums[forward_idx], nums[back_idx]])
                            ans_dict[[item, nums[forward_idx], nums[back_idx]]] = True

                        forward_idx += 1
                        back_idx -= 1
                    
                    elif nums[forward_idx] + nums[back_idx] < target:
                        forward_idx += 1
                    
                    elif nums[forward_idx] + nums[back_idx] > target:
                        back_idx -= 1
                checked_set.add(item)

        return ans


assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [
  [-1, 0, 1],
  [-1, -1, 2]
]