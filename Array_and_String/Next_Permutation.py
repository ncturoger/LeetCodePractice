class Solution(object):
    def nextPermutation(self, nums):
        pivot = len(nums) - 1
        while pivot > 0:
            if nums[pivot] > nums[pivot - 1]:
                swap_1 = pivot - 1
                sort_sub = nums[pivot:]
                sort_sub.sort()
                change_start = pivot
                for i in sort_sub:
                    nums[change_start] = i
                    change_start += 1
                i = pivot
                while nums[swap_1] >= nums[i]:
                    i += 1
                temp = nums[swap_1]
                nums[swap_1] = nums[i]
                nums[i] = temp
                return
            pivot -= 1

        nums.reverse()
        return


assert Solution().nextPermutation([1,2,3]) == [1,3,2]
assert Solution().nextPermutation([1]) == [1]