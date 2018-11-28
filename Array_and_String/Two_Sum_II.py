class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while(i < j):
            num_sum = numbers[i] + numbers[j]

            if target > num_sum:
                i += 1
            
            elif target < num_sum:
                j -= 1
            
            else:
                return [i+1, j+1]
        return -1