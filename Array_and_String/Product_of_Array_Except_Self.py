class Solution(object):
    # time exceed
    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        answer_list = []
        for idx, num in enumerate(nums):
            pr = 1
            for i in nums[:idx] + nums[idx + 1:]:
                pr *= i
            
            answer_list.append(pr)


        return answer_list


    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer_list = []
        for idx, num in enumerate(nums):
            answer_list.append(self.product_left(idx, nums) * self.product_right(idx, nums))

        return answer_list
    
    def product_left(self, i, nums):
        l = 1
        index = 0
        while index < i:
            l *= nums[index]
            index += 1
        
        return l
    
    def product_right(self, i, nums):
        r = 1
        index = i + 1
        while index < len(nums):
            r *= nums[index]
            index += 1
        
        return r


    def productExceptSelf_3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for i in nums]
        right = [1 for i in nums]
        ans = [1 for i in nums]

        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1] * nums[i -1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
            
            else:
                right[i] = right[i + 1] * nums[i + 1]
        
        for idx, val in enumerate(ans):
            ans[idx] = left[idx] * right[idx]
        

        return ans




assert Solution().productExceptSelf_3([1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf_3([0,0]) == [0,0]
assert Solution().productExceptSelf_3([1,1]) == [1,1]