class Solution(object):
    # over time
    def advantageCount_1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        result = []
        for item in B:
            idx = 0
            while idx < len(A) and A[idx] <= item:
                idx += 1
            if idx < len(A):
                result.append(A.pop(idx))
            else:
                result.append(A.pop(0))
        
        return result


    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        sorted_B = []
        adv_list = [None for i in B]
        
        for idx, val in enumerate(B):
            sorted_B.append((val, idx))
        
        sorted_B.sort()

        for item in A:
            if sorted_B:
                if item > sorted_B[0][0]:
                    adv_list[sorted_B[0][1]] = item
                    sorted_B.pop(0)
            else:
                break
        
        unused = list(set(A) - set(adv_list))
        print(unused)
        print(adv_list)

        if None in adv_list:
            if unused:
                for idx, item in enumerate(adv_list):
                    if item is None:
                        adv_list[idx] = unused.pop(0)

        return adv_list

assert Solution().advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
assert Solution().advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]
assert Solution().advantageCount([15,15,4,5,0,1,7,10,3,1,10,10,8,2,3], [4,13,14,0,14,14,12,3,15,12,2,0,6,9,0]) == [5,10,10,2,8,3,15,4,0,15,3,1,7,10,1]


