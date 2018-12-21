class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        arr = [str(i) for i in nums]
        sorted_arr = []
        answer = ""

        print("arr: {}, sorted: {}".format(nums, sorted_arr))
        for item_idx, item in enumerate(arr):
            is_inserted = False
            print(sorted_arr)
            for idx, num in enumerate(sorted_arr):
                i = 0
                min_len = min(len(num), len(item))
                while i < min_len and not is_inserted:
                    if item[i] > num[i]:
                        sorted_arr.insert(idx, item)
                        is_inserted = True
                        break
                   
                    if i == min_len - 1:
                        if item[i] == num[i]:
                            if len(item) - 1 > i:
                                if item[0] < item[i + 1]:
                                    sorted_arr.insert(idx, item)
                                    is_inserted = True
                                    break


                            elif  len(num) - 1 > i:
                                if num[0] > num[i + 1]:
                                    sorted_arr.insert(idx, item)
                                    is_inserted = True
                                    break
                    
                    if item[i] < num[i]:
                        break
                    
                    i += 1 

                
                if is_inserted:
                    break

            if not is_inserted:
                sorted_arr.append(item)
        print("arr: {}, sorted: {}".format(arr, sorted_arr))

        for num in sorted_arr:
            answer += num
        
        return str(int(answer))

assert Solution().largestNumber([10,2]) == "210"
assert Solution().largestNumber([3,30,34,5,9]) == "9534330"
assert Solution().largestNumber([121,12]) == "12121"
assert Solution().largestNumber([2,1]) == "21"
assert Solution().largestNumber([20,1]) == "201"
assert Solution().largestNumber([321,123]) == "321123"
assert Solution().largestNumber([824,8247]) == "8248247"