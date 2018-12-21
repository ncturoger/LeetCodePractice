class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finded_sub_set = [[]]
        select_nums = []
        self.find_sub(nums, 0, select_nums, finded_sub_set)
        print(finded_sub_set)
        return finded_sub_set


    def find_sub(self, nums, start_index, select_nums, finded_sub_set):
        print("nums:{}, start_index:{}, select_nums:{}, finded_sub_set:{}".format(
            nums, start_index, select_nums, finded_sub_set
        ))
        if start_index < len(nums):
            select_nums = [i for i in select_nums]
            select_num = nums[start_index]
            select_nums.append(select_num)
            if select_nums not in finded_sub_set:
                finded_sub_set.append(select_nums)

            for num in nums:
                self.find_sub(nums, start_index+1, select_nums, finded_sub_set)

Solution().subsetsWithDup([1,2,2])
